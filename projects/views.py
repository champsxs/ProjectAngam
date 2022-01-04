from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls.conf import path

from .models import Projects
from .forms import ProjectForm
# Create your views here.


def projects(request):
    projects = Projects.objects.all()
    context = {'projects': projects }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectobj = Projects.objects.get(id=pk)
    print(projectobj.review_set.all()[1].owner)
    tags = projectobj.tags.all()
    return render(request, 'projects/single.html', {'project': projectobj})


def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def updateProject(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')    
    context = {'object': project}
    return render(request, 'projects/delete_conf.html', context)