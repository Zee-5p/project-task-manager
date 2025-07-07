from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]