from django.shortcuts import render
from django.http import HttpResponse

#dammy projects
projects=[
    {
        'author':'Alex',
        'project_name':'Github',
        'project_description':'This is a site where you can search for github..'
    },
    {
        'author':'Alex',
        'project_name':'Github',
        'project_description':'This is a site where you can search for github..'
    },
]

def home(request):
    context = {
        'projects':projects
    }
    return render(request, 'awards/home.html', context)