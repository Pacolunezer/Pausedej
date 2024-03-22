from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Categorie
from .forms import ProduitForm
from panier.models import CartItem
from panier.views import view_cart
# Create your views here.
def home(request):
    produits= Product.objects.all()
    categories = Categorie.objects.all()
        # Assurez-vous que la fonction view_cart retourne un dictionnaire avec la clé 'total_quantity'
    context= {'produits': produits,'categories':categories}
    return render(request,'produits/listproduit.html', context)

# vifrom django.shortcuts import render, redirect
def a_propos(request):
 
    return render(request, 'base/Apropos.html')

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
def supprimer_produit(request, product_id):
    produit = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        produit.delete()
        return redirect('home')
    return render(request, 'produits/product_delete.html', {'produit':produit})
from .forms import RechercheProduitForm
from .models import Product  # Assurez-vous que vous importez correctement votre modèle Product

def rechercher_produits(request):
    if request.method == 'GET':
        form = RechercheProduitForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            
            # Recherchez tous les produits correspondant à la requête
            produits = Product.objects.filter(title__icontains=query)
            
            context = {
                'query': query,
                'produits': produits,
            }
            
            return render(request, 'produits/afficher_search.html', context)
    else:
        form = RechercheProduitForm()
        
    return render(request, 'product_search.html', {'form': form})


def commander_produit(request):
   return render(request, 'commandes/listcommande.html')