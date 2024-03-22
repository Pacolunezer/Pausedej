from django.urls import path
from . import views
urlpatterns= [
    path('', views.home, name= 'home'), 
    path('a_propos', views.a_propos, name='a_propos'),
    # URL pour la vue de détail du produit
    path('ajouter_produit/<int:product_id>/', views.ajouter_produit, name='ajouter_produit'),
    path('editer_produit/<int:product_id>/', views.editer_produit, name='editer_produit'),
    path('produits/<int:product_id>/', views.supprimer_produit, name='supprimer_produit'),
    #path('produits/update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    # Ajoutez l'URL pour la recherche de produits
    path('produits/', views.rechercher_produits, name='rechercher_produits')   
]