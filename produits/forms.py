from django import forms
from .models import Product,Categorie

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= [ 'category', 'title', 'price', 'description', 'quantity']


# forms.py
from django import forms

class RechercheProduitForm(forms.Form):
    q = forms.CharField(max_length=100, required=False, label='Terme de recherche')
    category = forms.ModelChoiceField(queryset=Categorie.objects.all(), empty_label="Toutes les catégories", required=False)