from django.urls import path
from  . import views as awards_views

urlpatterns = [
    path('', awards_views.home, name= 'home'),
    path('accounts/register', awards_views.register, name='registration')
]
