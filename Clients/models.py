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
        phone_number = models.CharField(max_length=9, blank=True)
        date_joined= models.DateTimeField(default=timezone.now)
       
        def __str__(self):
            return self.email
class Cart(models.Model):
    user = models.OneToOneField(CustomerUser, on_delete=models.CASCADE)
    # ... autres champs de votre panier ...

@receiver(post_save, sender=CustomerUser)
def create_user_cart(sender, instance, created, **kwargs):
     if created and not hasattr(instance, 'cart'):
        Cart.objects.create(user=instance)