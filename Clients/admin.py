
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser

class CustomUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ('email', 'prenom', 'nom', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('prenom', 'nom', 'phone_number')}),
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
