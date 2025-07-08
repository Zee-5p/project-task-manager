from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dashboard.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  # all app-level URLs handled here
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', home, name='home'),
    path('projects/', include('dashboard.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),]