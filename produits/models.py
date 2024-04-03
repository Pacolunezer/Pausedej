from typing import Any
from django.db import models

# Create your models here.
class Categorie(models.Model):
   name= models.CharField(max_length=200, null=True)
   def __str__(self):
       return self.name
class Product(models.Model):
    image= models.ImageField(upload_to='images/')
    title= models.CharField(max_length=150,null=True)
    price= models.FloatField(default=0.0)
    quantity=models.PositiveIntegerField(default=0)
    description=models.CharField(max_length=300,null=True)
    category=models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class  Collection(models.Model):
    img= models.ImageField(upload_to='images/')
    titre= models.CharField(max_length=200, null=True)
    descriptions= models.CharField(max_length=200,null=True)
    prix= models.FloatField(default=0.0)
    categorie= models.ForeignKey(Categorie, on_delete=models.CASCADE)
    def __str__(self) :
        return self.titre
    