from django.urls import path
from  . import views as awards_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', awards_views.home, name= 'home'),
    path('accounts/register', awards_views.register, name='register'),
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
]
