from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import UserRegisterForm

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
            return redirect('home')
    else:
        form= UserRegisterForm()  
    return render(request, 'registration/registration.html', {'form':form})