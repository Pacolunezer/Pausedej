from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem
from django.contrib import messages
from django.http import JsonResponse

@login_required
def update_cart(request, product_id):
    if request.method == 'POST':
        # Récupérez la nouvelle quantité envoyée par l'utilisateur
        new_quantity = int(request.POST.get('quantity'))
        
        # Récupérez le cart_item correspondant au produit
        cart_item = CartItem.objects.get(user=request.user, product_id=product_id)
        
        # Mettez à jour la quantité du produit dans le panier
        cart_item.quantity = new_quantity
        cart_item.save()
        
        # Retournez une réponse JSON pour indiquer que la mise à jour a réussi
        return JsonResponse({'success': True})
    else:
        # Si la requête n'est pas de type POST, retournez une réponse JSON avec une erreur
        return JsonResponse({'error': 'Method not allowed'}, status=405)

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
    
    # Redirigez l'utilisateur vers la page de détail du panier
    return redirect('home')

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
