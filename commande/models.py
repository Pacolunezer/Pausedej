from django.db import models

# Create your models here.
from django.db import models
from produits.models import Product

class Commande(models.Model):
    prenom = models.CharField(max_length=200, null=True)
    nom = models.CharField(max_length=200, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)  # Le champ s'appelle "ville"
    code_pays_choices = [
        ('+1', '+1 - USA'),
        ('+44', '+221 - SN'),
        ('+33', '+33 - France'),
        # Ajoutez d'autres codes de pays au besoin
    ]
    code_pays = models.CharField(max_length=5, choices=code_pays_choices)
    numero_telephone = models.CharField(max_length=9)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Champ total_amount ajouté
    livre = models.BooleanField(default=False) 
    def __str__(self):
        return self.prenom

    def calculer_total(self):
        total = 0
        items = self.commandeitem_set.all()  # Récupère tous les éléments de commande associés à cette commande
        for item in items:
            total += item.produit.prix * item.quantite  # Calcule la somme totale en ajoutant le prix du produit multiplié par la quantité
        return total