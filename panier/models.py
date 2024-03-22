from django.db import models

# Create your models here.
# cart/models.py

from django.db import models
from django.conf import settings
from produits.models import Product  # Assurez-vous que vous avez déjà créé le modèle Product
from django.contrib.auth.models import User
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    
        
    def subtotal(self):
       
        return self.quantity * self.product.price
    # cart/views.py
