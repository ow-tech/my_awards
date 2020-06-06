from django.urls import path
from  . import views as awards_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', awards_views.home, name= 'home'),
    path('accounts/register', awards_views.register, name='register'),
    path('accounts/profile', awards_views.profile, name='profile'),
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)