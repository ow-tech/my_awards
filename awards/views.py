from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm

#dammy projects

def home(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'awards/home.html', context)

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form= UserRegisterForm()  
    return render(request, 'registration/registration.html', {'form':form})
@login_required
def profile(request):
    # images = Image.objects.filter(author=request.user).all()
    profile = Profile.objects.get_or_create(user=request.user)
    if request.method =='POST':
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('profile')
    else:
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    context = {
        'profile_update_form': profile_update_form,
        # 'projects':projects
    }
    return render(request, 'registration/profile.html', context)