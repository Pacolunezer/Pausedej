from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser, Postulation

class CustomUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ('email', 'prenom', 'nom', 'numero_telephone', 'date_joined', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('prenom', 'nom', 'numero_telephone', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'prenom', 'nom')
    ordering = ('email',)

admin.site.register(CustomerUser, CustomUserAdmin)

class PostulationAdmin(admin.ModelAdmin):  # Correction du nom de la classe
    model = Postulation
    list_display = ('nom', 'prenom', 'email', 'cv')

admin.site.register(Postulation, PostulationAdmin)
