from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['prenom', 'nom', 'ville', 'email',  'adresse', 'zipcode', 'livre']
