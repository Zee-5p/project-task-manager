from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:project_pk>/tasks/', views.task_list, name='task_list'),
    path('projects/<int:project_pk>/tasks/add/', views.add_task, name='add_task'),
    path('projects/<int:project_pk>/tasks/<int:task_pk>/edit/', views.edit_task, name='edit_task'),
    path('projects/<int:project_pk>/tasks/<int:task_pk>/delete/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:project_pk>/tasks/add/', views.add_task, name='add_task'),]