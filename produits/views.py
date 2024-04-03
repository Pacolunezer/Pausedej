from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Categorie, Collection
from .forms import ProduitForm
from panier.models import CartItem
from django.contrib.auth.decorators import login_required
from panier.views import view_cart
from django.db.models import Sum 
# Create your views here.
def home(request):
    produits= Product.objects.all()
    categories = Categorie.objects.all()
    product= Collection.objects.all()
        # Calculer la quantité totale du panier
    total_quantity = 0
    if request.user.is_authenticated:
        total_quantity = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

    # Ajouter la quantité totale du panier au contexte
    context = {'produits': produits, 'categories': categories, 'product':product,
               'total_quantity': total_quantity}
    
    return render(request,'produits/listproduit.html', context)

# vifrom django.shortcuts import render, redirect
def a_propos(request):
        # Calculer la quantité totale du panier
    total_quantity = 0
    if request.user.is_authenticated:
        total_quantity = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

    # Ajouter la quantité totale du panier au contexte
    context = { 'total_quantity': total_quantity}
    return render(request, 'base/Apropos.html', context)

def ajouter_produit(request, product_id):
    # Récupérez le produit à afficher (par exemple, le produit avec l'ID 1)
    
    produit = Product.objects.get(pk=product_id)  # Remplacez 1 par l'ID du produit que vous souhaitez afficher
    if request.method == 'POST':
        produit.add()
        return redirect('home')
    return render(request, 'produits/product_add.html', {'produit': produit })

def editer_produit(request, product_id):
    produit= get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form =ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save() 
            return redirect('ajouter_produit')
    else: 
        form= ProduitForm(instance=produit)
        return render(request, 'produits/product_edit.html', {'form': form, 'produit':produit})
    

@login_required
def supprimer_produit(request, product_id):
    produit = get_object_or_404(Product, pk=product_id)
    total_quantity = 0
    if request.method == 'POST':
        produit.delete()
        return redirect('home')
    if request.user.is_authenticated:
        total_quantity = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        cart_items = CartItem.objects.filter(user=request.user)  # Récupérer les éléments de panier pour l'utilisateur actuel

    context = {
        'total_quantity': total_quantity,
        'produit': produit, 
        'cart_items': cart_items
    }
    return render(request, 'produits/product_delete.html', context)

from .forms import RechercheProduitForm
from .models import Product  # Assurez-vous que vous importez correctement votre modèle Product


def rechercher_produits(request):
    if request.method == 'GET':
        form = RechercheProduitForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            produits = Product.objects.filter(title__icontains=query)
            total_quantity = 0
            if request.user.is_authenticated:
                total_quantity = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

            context = {
                'query': query,
                'total_quantity': total_quantity,
                'produits': produits,
            }
            return render(request, 'produits/afficher_search.html', context)
        else:
            # Le formulaire n'est pas valide, donc nous retournons une page vide
            return render(request, 'produits/afficher_search.html', {})
    else:
        form = RechercheProduitForm()
        return render(request, 'product_search.html', {'form': form})


def commander_produit(request):
   return render(request, 'commandes/listcommande.html')