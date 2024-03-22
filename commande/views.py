from django.shortcuts import render, redirect, HttpResponse
from .models import Commande
from .forms import CommandeForm  # Assurez-vous d'avoir un fichier forms.py avec votre formulaire
from panier.views import view_cart, CartItem

def convert_cfa_to_usd(amount_in_xof):
    # Définissez votre taux de change fixe
    taux_de_change = 0.0015  # Par exemple, 1 USD = 550 XOF

    # Convertir la somme en XOF en USD en utilisant le taux de change
    amount_in_usd = amount_in_xof * taux_de_change
    return amount_in_usd

def commande_view(request):
     # Initialisez le total_amount à 0 par défaut

    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigez l'utilisateur après avoir sauvegardé la commande
        return redirect('commande_view')
    else:
        form = CommandeForm()
        cart_items = CartItem.objects.filter(user=request.user)
        # Calculez la somme totale des produits dans le panier
        total_amount = sum(item.product.price * item.quantity for item in cart_items)
          # Supposons que vous avez déjà récupéré la somme en XOF
        somme_en_xof = total_amount # Par exemple, la somme en XOF récupérée de votre panier
    # Convertir la somme en XOF en USD
        somme_en_usd = convert_cfa_to_usd(total_amount)
        somme_en_usd = round(somme_en_usd, 2)  # Arrondir le montant à deux décimales


    context = {
        'form': form,
        'total_amount': total_amount,
        'cart_items': cart_items,
        'somme_en_usd':somme_en_usd
    }
    return render(request, 'commandes/listcommande.html', context)


def commandes_livre(request):
    commandes_livre = Commande.objects.filter(livre=True)
    
    # Faites quelque chose avec les commandes livrées (par exemple, les afficher)
    
    # ...
    
    return HttpResponse("Liste des commandes livrées : {}".format(commandes_livre))

def commandes_non_livre(request):
    commandes_non_livre = Commande.objects.filter(livre=False)
    
    # Faites quelque chose avec les commandes non livrées (par exemple, les afficher)
    
    # ...
    
    return HttpResponse("Liste des commandes non livrées : {}".format(commandes_non_livre))