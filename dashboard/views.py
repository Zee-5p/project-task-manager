from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from .models import Task 

@login_required
def project_list(request):
    # Show only the projects created by the current user
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'dashboard/project_list.html', {'projects': projects})

@login_required
def edit_project(request, pk):
    # Only allow the user to edit their own project
    project = get_object_or_404(Project, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'dashboard/edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    
    return render(request, 'dashboard/confirm_delete.html', {'project': project})

@login_required
def task_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk, created_by=request.user)
    tasks = Task.objects.filter(project=project)
    return render(request, 'dashboard/task_list.html', {'project': project, 'tasks': tasks})