from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

projectList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'fully functional ecommerce website',
        'topRated': True,
    },
    {
        'id': '2',
        'title':'Portfolio website',
        'description':'A personal website to write artivles and display',
        'topRated': False,
    },
    {   'id': '3',
        'title':'Social Network',
        'description':'An open source project built by the commnunity',
        'topRated': True,
        },
]



def home(request):
    projects = Project.objects.all() 
    context = {'projects': projects}
    return render(request, 'blog/home.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    
    return render(request, 'blog/single-project.html',{ 'project': projectObj} )


