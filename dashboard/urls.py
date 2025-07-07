from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:project_pk>/tasks/', views.task_list, name='task_list'),
    path('projects/<int:project_pk>/tasks/add/', views.add_task, name='add_task'),
]