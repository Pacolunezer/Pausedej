from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomerUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ['email', 'prenom', 'nom', 'password1', 'password2', 'phone_number']

    widgets = {
        'username': forms.TextInput(),
        'email': forms.EmailInput(),
    }

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
