from django.contrib import admin
from .models import Product, Categorie,Collection
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
     list_display= ('name',)

class AdminProduct(admin.ModelAdmin):
     list_display= ('category', 'image', 'title','price','quantity')

class AdminCollection(admin.ModelAdmin):
     list_display= ('titre','img', 'descriptions', 'categorie', 'prix')

admin.site.register(Collection, AdminCollection)  
admin.site.register(Product, AdminProduct)   
admin.site.register(Categorie, AdminCategorie)


