from django import forms
from .models import Product,Categorie, Collection

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= [ 'category', 'title', 'price', 'description', 'quantity']


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields= [ 'img', 'descriptions', 'categorie', 'prix']


# forms.py
from django import forms

class RechercheProduitForm(forms.Form):
    q = forms.CharField(max_length=100, required=False, label='Terme de recherche')
    category = forms.ModelChoiceField(queryset=Categorie.objects.all(), empty_label="Toutes les catégories", required=False)
    def clean_q(self):
        q = self.cleaned_data.get('q', '').strip()
        if not q:
            raise forms.ValidationError("Le champ de recherche ne peut pas être vide.")
        self.query = q 
        return q