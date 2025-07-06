from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required
def project_list(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'dashboard/project_list.html', {'projects': projects})