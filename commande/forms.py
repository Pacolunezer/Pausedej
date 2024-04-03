from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        numero_telephone = cleaned_data.get('numero_telephone')
        if Commande.objects.filter(numero_telephone=numero_telephone).exists():
            self.add_error('numero_telephone', "Ce numéro de téléphone existe déjà.")
        return cleaned_data

    class Meta:
        model = Commande
        fields = ['prenom', 'nom', 'ville', 'email',  'adresse', 'code_pays', 'numero_telephone', 'livre']
