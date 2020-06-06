from django.urls import path
from  . import views as awards_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', awards_views.home, name= 'home'),
    path(r'accounts/register', awards_views.register, name='register'),
    path(r'accounts/profile', awards_views.profile, name='profile'),
    path(r'accounts/login', auth_views.LoginView.as_view(), name='login'),
    path(r'accounts/logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path(r'new/project', awards_views.new_project, name='new-project'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)