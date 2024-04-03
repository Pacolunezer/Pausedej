# cart/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import add_to_cart, clear_cart, view_cart, supprimer_panier

urlpatterns = [
    # ... d'autres URLs ...
      path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
      path('supprimer_panier/<int:product_id>/', supprimer_panier, name='supprimer_panier'),
      path('view_cart', view_cart, name='view_cart'),
      path('clear-cart/', clear_cart, name='clear_cart'),
      path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
       
      
]
