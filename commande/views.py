from django.shortcuts import render, redirect, HttpResponse
from .models import Commande
from .forms import CommandeForm
from panier.models import CartItem
from django.db.models import Sum
def convert_cfa_to_usd(amount_in_xof):
    # Définissez votre taux de change fixe
    taux_de_change = 0.0015  # Par exemple, 1 USD = 550 XOF

    # Convertir la somme en XOF en USD en utilisant le taux de change
    amount_in_usd = amount_in_xof * taux_de_change
    return amount_in_usd
from django.db.models import Sum

def commande_view(request):
    form = CommandeForm()
    cart_items = []
    total_quantity = 0
    total_amount = 0
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
        
             cart_items = CartItem.objects.filter(user=request.user)
             total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity']
             total_amount = sum(item.product.price * item.quantity for item in cart_items)
             commande = form.save(commit=False)
             commande.total_amount= total_amount
             commande.total_quantity = total_quantity
             commande.save()

             return redirect('home')

    # Si le formulaire n'est pas valide ou si la méthode de la requête est GET
    # Nous calculons toujours la somme totale de la quantité des produits dans le panier
    cart_items = CartItem.objects.filter(user=request.user)
    total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity']

    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    somme_en_xof = total_amount
    somme_en_usd = convert_cfa_to_usd(total_amount)
    somme_en_usd = round(somme_en_usd, 2)

    context = {
        'form': form,
        'total_amount': total_amount,
        'total_quantity': total_quantity,
        'cart_items': cart_items,
        'somme_en_usd': somme_en_usd
    }
    return render(request, 'commandes/listcommande.html', context)
