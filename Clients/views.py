from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import LoginForm 
from django.shortcuts import render, redirect 
from .models import CustomerUser
from django.contrib import messages
from .forms import CustomUserCreationForm  # Vous devez créer ce formulaire
@login_required
def signup(request):
    if request.method == 'POST':
        form = CustomerUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirigez l'utilisateur après l'inscription
    else:
        form = CustomUserCreationForm()
    return render(request, 'clients/signup.html', {'form': form})

# views.py

@login_required
def profile(request):
    # mon code pour afficher le profil de l'utilisateur ici
    context = {'username': request.user}
    return render(request, 'clients/profile.html', context)  # Assurez-vous d'avoir un modèle de profil (profile.html)

def account_views(request):
    context= {'user':request.user }
    return render(request, 'clients/account.html', context)

@login_required
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']  # Utilisez le champ approprié pour le nom d'utilisateur
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirigez vers la page du tableau de bord après la connexion
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
    else:
        form = LoginForm()

    return render(request, 'clients/login.html', {'form': form})
from django.contrib.auth import logout  # Ajoutez ceci à vos imports

@login_required
def logout_view(request):
   logout(request)
   return redirect('login_view')