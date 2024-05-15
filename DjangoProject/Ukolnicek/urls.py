"""
URL configuration for Ukolnicek project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UkolnicekApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/loginUser', views.loginUser, name='loginUser'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('register/registerUser', views.registerUser, name='registerUser'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('friends/<int:user_id>/', views.friends, name='friends'),
    path('userlist/<int:project_id>/', views.userlist, name='userlist'),
    path('project/<int:project_id>/', views.project, name="project"),
    path('task/<int:task_id>/', views.task, name="task"),
    path('addTask/<int:project_id>/', views.addTask, name='addTask'),
    path('editTask/<int:task_id>/', views.editTask, name='editTask'),
    path('addProject/', views.addProject, name='addProject'),
    path('editProject/<int:project_id>/', views.editProject, name='editProject'),
    path('project/addUserToProject/<int:project_id>/', views.addUserToProject, name='addUserToProject'),
    path('addUserToTask/<int:task_id>/', views.addUserToTask, name='addUserToTask'),
]
