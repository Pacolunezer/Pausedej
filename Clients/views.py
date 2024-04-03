from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, LoginForm
from .forms import PostulationForm
from django.contrib import messages

#////// ¨Posstulation


def postuler(request):
    if request.method == 'POST':
        form = PostulationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = PostulationForm()
    return render(request, 'clients/postulation.html', {'form': form})

def confirmation(request):
    # Ajoutez des données spécifiques à afficher dans le modèle de confirmation
    confirmation_message = "Votre candidature a été soumise avec succès."
    return render(request, 'clients/confirmation.html', {'confirmation_message': confirmation_message})


@login_required
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Inscription réussie. Vous êtes maintenant connecté.')
            return redirect('profile')  # Redirigez l'utilisateur après l'inscription
    else:
        form = CustomUserCreationForm()
         
    return render(request, 'clients/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'clients/profile.html', {'user': request.user})

@login_required
def account_views(request):
    return render(request, 'clients/account.html', {'user': request.user})

@login_required
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['email']  # Assurez-vous que 'email' est le nom du champ email dans le formulaire LoginForm
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirigez vers la page du profil après la connexion
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
    else:
        form = LoginForm()

    return render(request, 'clients/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')
