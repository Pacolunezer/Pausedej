# monapp/urls.py
from django.urls import path
from . import views  

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login-view/', views.login_view, name='login_view'),
    path('account_view/', views.account_views, name='account_views'),
    path('logout/', views.logout_view, name='logout'),
    path('postuler/', views.postuler, name='postuler'),
    path('confirmation/', views.confirmation, name='confirmation'),
    # ... d'autres URL de votre application ...
]
