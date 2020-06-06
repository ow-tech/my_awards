from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, NewProjectForm

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
@login_required()
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
@login_required()
def new_project(request):
    current_user =request.user
    form = NewProjectForm(request.POST, request.FILES)
    if form.is_valid():
        project = form.save(commit=False)
        project.author = current_user
        project.save_project()
        return redirect('home')
    else:
        form = NewProjectForm(request.POST, request.FILES)
    return render (request, 'awards/new_project.html', {"form":form})