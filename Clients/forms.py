from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser
from django.utils import timezone

from django import forms
from .models import Postulation

class CustomUserCreationForm(UserCreationForm):
    date_joined = forms.CharField(label='Date joined', required=False)
    class Meta:
        model = CustomerUser
        fields = ['email', 'prenom', 'nom', 'numero_telephone','password1', 'password2','date_joined']

    widgets = {
        'username': forms.TextInput(),
        'email': forms.EmailInput(),
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Formatage de la date de création pour l'affichage dans le formulaire
        self.fields['date_joined'].initial = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fields['date_joined'].widget.attrs['readonly'] = True

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class PostulationForm(forms.ModelForm):
    class Meta:
        model = Postulation
        fields = ['nom', 'prenom', 'email', 'cv']
