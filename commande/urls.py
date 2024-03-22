from django.urls import path
from .views import commande_view
urlpatterns = [
    # ...
     path('commande/', commande_view, name='commande_view'),
]
