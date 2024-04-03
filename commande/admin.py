from django.contrib import admin
from .models import     Commande

# Register your models here.

class AdminCommande(admin.ModelAdmin):
    list_display= ('prenom', 'nom', 'date_commande', 'livre', 'email', 'ville',  'adresse', 'numero_telephone', 'code_pays', 'total_amount')

admin.site.register(Commande, AdminCommande)