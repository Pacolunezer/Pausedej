from django.db import models

# Create your models here.
from django.db import models
from produits.models import Product

class Commande(models.Model):
    prenom = models.CharField(max_length=200, null=True)
    nom = models.CharField(max_length=200, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    adresse = models.CharField(max_length=200, unique=True)
    ville = models.CharField(max_length=200, unique=True)  # Le champ s'appelle "ville"
    zipcode = models.CharField(max_length=200, unique=True)
    livre = models.BooleanField(default=False) 