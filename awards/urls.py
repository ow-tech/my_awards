from django.urls import path
from  . import views as awards_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', awards_views.home, name= 'home'),
    path('accounts/register', awards_views.register, name='register'),
    path('accounts/profile', awards_views.profile, name='profile'),
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('new/project', awards_views.new_project, name='new-project'),
    path('single/(<int:pk>)/', awards_views.single_project, name = 'single_project'),
    path('search/', awards_views.search_results, name='search_results'),
    path('project/(<int:pk>)/', awards_views.review, name='review'),
    path('profile_list/', awards_views.profile_list.as_view()),
    path('project_list', awards_views.project_list.as_view()),
]