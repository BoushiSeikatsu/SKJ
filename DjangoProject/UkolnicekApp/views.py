from django.shortcuts import *
from django.http import HttpResponse
from .models import *
from .forms import *
from datetime import datetime

# Create your views here.

def isUserLoggedIn(request):
    if ("username" not in request.session):
        request.session["username"] = None
        request.session["user_id"] = None
    if (request.session["username"] != None):
        return True
    return False
def index(request):
    userId = 0
    projectsFiltered = []
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
        projects = Projekt.objects.all()
        for project in projects:
            if(project.uzivatel.uzivatel_id == request.session["user_id"]):
                projectsFiltered.append(project)
    return render(request, 'UkolnicekApp/index.html', {'projects': projectsFiltered, 'loggedIn': loggedIn, 'userId': userId})

def login(request):
    loggedIn = isUserLoggedIn(request)
    loginForm = LoginForm()
    return render(request,'UkolnicekApp/login.html', {'loginForm' : loginForm, 'loggedIn': loggedIn} )

def loginUser(request):
    if(request.method == 'POST'):
        loginForm = LoginForm(request.POST)
        if(loginForm.is_valid()):
            loginBody = loginForm.cleaned_data
            userExists = Uzivatel.objects.filter(uzivatelske_jmeno=loginBody["uzivatelske_jmeno"])
            if(userExists.exists()):
                user = get_object_or_404(Uzivatel,uzivatelske_jmeno=loginBody["uzivatelske_jmeno"])
                if(user.heslo == loginBody["heslo"]):
                    request.session["username"] = user.uzivatelske_jmeno
                    request.session["user_id"] = user.uzivatel_id
                    return redirect('index')

def logout(request):
    request.session["username"] = None
    request.session["user_id"] = None
    return redirect('index')

def register(request):
    loggedIn = isUserLoggedIn(request)
    registerForm = RegisterForm()
    return render(request, 'UkolnicekApp/register.html', {'registerForm' : registerForm, 'loggedIn': loggedIn})

def registerUser(request):
    if (request.method == 'POST'):
        registerForm = RegisterForm(request.POST)
        if (registerForm.is_valid()):
            registerBody = registerForm.cleaned_data
            role = get_object_or_404(Role, pk=3)
            userExists = Uzivatel.objects.filter(uzivatelske_jmeno=registerBody["uzivatelske_jmeno"])
            if(not userExists.exists()):
                user = Uzivatel(posledni_zmena=datetime.now(), datum_vytvoreni=datetime.now(), uzivatelske_jmeno=registerBody["uzivatelske_jmeno"], krestni_jmeno=registerBody["krestni_jmeno"], prijmeni=registerBody["prijmeni"], heslo=registerBody["heslo"], email=registerBody["email"], role=role, posledni_login=datetime.now(), prihlasen=False)
                user.save()
                return redirect('index')
        

def about(request):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    return render(request, 'UkolnicekApp/about.html', {'loggedIn': loggedIn, 'userId': userId})

def faq(request):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    return render(request, 'UkolnicekApp/faq.html', {'loggedIn': loggedIn, 'userId': userId})

def user(request, user_id):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    user = get_object_or_404(Uzivatel, pk=user_id)
    return render(request, 'UkolnicekApp/user.html', {'user': user, 'loggedIn': loggedIn, 'userId': userId})#userId je tady kvuli base layout navigaci, pouziva se pro vsechny views

def friends(request, user_id):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    return render(request, 'UkolnicekApp/friends.html', {'loggedIn': loggedIn, 'userId': userId})

def userlist(request, project_id):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    usersInProject = []
    connections = UzivatelProjekt.objects.all()
    project = Projekt.objects.get(pk=project_id)
    for connection in connections:
        if(connection.projekt.projekt_id == project_id):
            usersInProject.append(connection.uzivatel)
    userTaskCount = []
    for user in usersInProject:
        tasks = Ukol.objects.filter(uzivatel=user,projekt=project)
        if(tasks.exists()):
            
            userTaskCount.append((user.uzivatelske_jmeno,len(tasks)))
        else:
            userTaskCount.append((user.uzivatelske_jmeno,0))
    return render(request, 'UkolnicekApp/userlist.html', {'project_id': project_id , 'userTaskCount': userTaskCount, 'loggedIn': loggedIn, 'userId': userId})

def project(request, project_id):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    project = get_object_or_404(Projekt, pk=project_id)
    tasks = Ukol.objects.filter(projekt=project_id)
    return render(request, 'UkolnicekApp/project.html', {'project': project, 'tasks': tasks, 'loggedIn': loggedIn, 'userId': userId})

def addProject(request):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    return render(request, 'UkolnicekApp/addProject.html', {'loggedIn': loggedIn, 'userId': userId})

def editProject(request, project_id):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    return render(request, 'UkolnicekApp/editProject.html', {'loggedIn': loggedIn, 'userId': userId})

def task(request, task_id):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    task = get_object_or_404(Ukol, pk=task_id)
    return render(request, 'UkolnicekApp/task.html', {'task': task, 'project_id': task.projekt.projekt_id, 'loggedIn': loggedIn, 'userId': userId})

def addTask(request):
    loggedIn = isUserLoggedIn(request)
    if (loggedIn):
        userId = request.session["user_id"]
    return render(request, 'UkolnicekApp/addTask.html', {'loggedIn': loggedIn, 'userId': userId})

def editTask(request, task_id):
    if (request.method == 'POST'):
        task = get_object_or_404(Ukol, pk = task_id)
        editTaskForm = EditTaskForm(request.POST, instance=task)
        if (editTaskForm.is_valid()):
            editTaskForm.save()
            return redirect('project', task.projekt.projekt_id)
    else:
        loggedIn = isUserLoggedIn(request)
        task = get_object_or_404(Ukol, pk = task_id)
        editTaskForm = EditTaskForm(instance=task)
        if (loggedIn):
            userId = request.session["user_id"]
        return render(request, 'UkolnicekApp/editTask.html', {'editTaskForm': editTaskForm, 'task_id': task_id, 'loggedIn': loggedIn, 'userId': userId})

def addUserToProject(request, project_id):
    if (request.method == 'POST'):
        addUserForm = UserProjectForm(request.POST)
        if (addUserForm.is_valid()):
            addUserFormBody = addUserForm.cleaned_data
            userExists = Uzivatel.objects.filter(uzivatelske_jmeno=addUserFormBody["uzivatelske_jmeno"])
            if(userExists.exists()):
                user = Uzivatel.objects.get(uzivatelske_jmeno=addUserFormBody["uzivatelske_jmeno"])
                project = Projekt.objects.get(projekt_id = project_id)
                connection = UzivatelProjekt(uzivatel=user, projekt=project)
                connection.save()
                return redirect('project', project_id)
    else:
        loggedIn = isUserLoggedIn(request)
        addUserForm = UserProjectForm()
        if (loggedIn):
            userId = request.session["user_id"]
        return render(request, 'UkolnicekApp/addUserToProject.html', {'addUserForm' : addUserForm, 'project_id': project_id, 'loggedIn': loggedIn, 'userId': userId})


