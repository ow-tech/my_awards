from django.shortcuts import render, redirect, get_object_or_404
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

def single_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    context = {
        "project":project
    }
    return render(request,'awards/single_project.html', context )
def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term= request.GET.get('project')
        searched_projects = Project.search_by_project_name(search_term)
        message = f"{ search_term }"
        return render (request, 'awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awards/search.html',{"message":message})
