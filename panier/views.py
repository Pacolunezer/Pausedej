from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def add_to_cart(request, product_id):
    # Récupérez le produit à ajouter
    product = get_object_or_404(Product, id=product_id)
    
    # Vérifiez si le produit existe déjà dans le panier de l'utilisateur
    cart_item = CartItem.objects.filter(user=request.user, product=product).first()
    
    if cart_item:
        # Si le produit existe déjà, augmentez simplement la quantité
        cart_item.quantity += 1
        cart_item.save()
    else:
        # Si le produit n'existe pas, créez un nouvel objet CartItem avec une quantité de 1
        cart_item = CartItem.objects.create(user=request.user, product=product, quantity=1)
    
    # Redirigez l'utilisateur vers la page précédente
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))

@login_required
def view_cart(request):
    # Récupérez tous les articles du panier de l'utilisateur connecté
    cart_items = CartItem.objects.filter(user=request.user)
    total_quantity = sum(item.quantity for item in cart_items)
    
    # Calculez le sous-total en parcourant tous les articles du panier
    subtotal = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total_quantity': total_quantity
    }

    return render(request, 'Panier/cart_detail.html', context)

@login_required
def clear_cart(request):
    user = request.user

    # Supprimez tous les éléments du panier pour l'utilisateur actuel
    CartItem.objects.filter(user=user).delete()

    # Redirigez l'utilisateur vers une page appropriée (par exemple, la page d'accueil)
    return redirect('home')  # Remplacez 'home' par le nom de la vue où vous souhaitez rediriger l'utilisateur après avoir vidé le panier
from django.db.models import Sum
@login_required
def supprimer_panier(request, product_id):
    # Récupérez l'objet CartItem correspondant au produit dans le panier de l'utilisateur connecté
    cart_items = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    
    if request.method == 'POST':
        # Supprimez l'objet CartItem
        cart_items.delete()
        messages.success(request, "Le produit a été supprimé du panier avec succès.")
        return redirect('view_cart')  # Redirigez l'utilisateur vers la page du panier ou toute autre page appropriée
    else:
        # Si la méthode n'est pas POST, retournez une réponse indiquant que cette méthode n'est pas autorisée
        total_quantity=0
        if request.user.is_authenticated:
          total_quantity = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    
        context={'total_quantity':total_quantity, 'cart_items':cart_items}
        return render(request, 'produits/product_delete.html', context)