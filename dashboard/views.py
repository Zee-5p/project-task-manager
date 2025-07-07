from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def project_list(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'dashboard/project_list.html', {'projects': projects})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'dashboard/edit_project.html', {'form': form, 'project': project})