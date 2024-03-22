from django.contrib import admin
from .models import Product, Categorie
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
     list_display= ('name',)

class AdminProduct(admin.ModelAdmin):
     list_display= ('category', 'image', 'title','price','quantity')


admin.site.register(Product, AdminProduct)   
admin.site.register(Categorie, AdminCategorie)


