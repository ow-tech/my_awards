from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project, Profile, Review
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, NewProjectForm, ReviewForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import profileSerializer


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
    images = Image.objects.filter(author=request.user).all()
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
        'projects':projects
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
@login_required()
def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term= request.GET.get('project')
        searched_projects = Project.search_by_project_name(search_term)
        message = f"{ search_term }"
        return render (request, 'awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awards/search.html',{"message":message})

@login_required()
def review(request,pk):
    user=request.user
    project = Project.objects.get(id=pk)
    reviews = Review.objects.filter(user=request.user, project_id=pk)
    print(project)
    print(reviews)
    rating_status = None
    if reviews is None:
        rating_status = False
    else:
        rating_status = True
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.project = project
            review.save()

            project_reviews = Review.objects.filter(project=project)


            design_ratings = [d.design for d in project_reviews]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in project_reviews]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in project_reviews]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            review.design_average = round(design_average, 2)
            review.usability_average = round(usability_average, 2)
            review.content_average = round(content_average, 2)
            review.score = round(score, 2)
            review.save()

            return redirect('home')
        else:
            form = ReviewForm(request.POST)
        context = {
            "form":form,
            "project":project
        }
        return render(request, 'awards/single_project.html', context)
class profile_list(APIView):
    def get(self, request):
        profile = Profile.objects.all()
        serializer = profileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
