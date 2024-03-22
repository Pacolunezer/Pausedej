from django.contrib import admin
from .models import     Commande

# Register your models here.

class AdminCommande(admin.ModelAdmin):
    list_display= ('prenom', 'nom', 'date_commande', 'livre', 'email',  'adresse', 'zipcode')

admin.site.register(Commande, AdminCommande)