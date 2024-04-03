from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Projekt, Ukol

# Create your views here.
def index(request):
    projects = Projekt.objects.all()
    return render(request, 'UkolnicekApp/index.html', {'projects': projects})

def login(request):
    pass

def register(request):
    pass

def about(request):
    pass

def faq(request):
    pass

def user(request, user_id):
    pass

def friends(request, user_id):
    pass

def userlist(request):
    pass

def project(request, project_id):
    project = get_object_or_404(Projekt, pk=project_id)
    tasks = Ukol.objects.filter(projekt=project_id)
    return render(request, 'UkolnicekApp/projekt.html', {'project': project, 'tasks': tasks})

def addProject(request):
    pass

def editProject(request, project_id):
    pass

def task(request, task_id):
    pass

def addTask(request):
    pass

def editTask(request, task_id):
    pass