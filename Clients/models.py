from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class CustomerUser(AbstractUser):
        email= models.EmailField(unique=True)
        prenom= models.CharField(max_length=30, blank=True)
        nom= models.CharField(max_length=30, blank=True) 
        numero_telephone = models.CharField(max_length=9, blank=True)
        date_joined= models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.email
class Cart(models.Model):
    user = models.OneToOneField(CustomerUser, on_delete=models.CASCADE)
    # ... autres champs de votre panier ...

@receiver(post_save, sender=CustomerUser)
def create_or_update_cart(sender, instance, created, **kwargs):
    if created:
        # L'utilisateur vient d'être créé, donc nous créons un panier pour lui
        Cart.objects.create(user=instance)
    else:
        # L'utilisateur existe déjà, nous mettons à jour le panier s'il existe
        if hasattr(instance, 'cart'):
            cart = instance.cart
            # Mettre à jour les champs du panier si nécessaire
            cart.save()
        else:
            # L'utilisateur n'a pas de panier, donc nous le créons
            Cart.objects.create(user=instance)


class Postulation(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.FileField(upload_to='cv/')

    def __str__(self):
        return f"{self.nom} {self.prenom}"
