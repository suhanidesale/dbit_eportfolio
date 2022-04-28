from django.shortcuts import render , redirect
from django.http import HttpResponse
from numpy import place
from .models import Project , Internship
from .forms import ProjectForm , internshipForm

def projects(request):
    projects = Project.objects.all()
    context ={ 'projects': projects}
    return render(request,'projects/projects.html',context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
   
    print('projectObj:',projectObj)
    return render(request,'projects/single-project.html',{'project':projectObj})

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html",context )

def updateeProject(request , pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES , instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html",context )

def deleteProject(request,pk):
    project= Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context ={'object': project}
    return render(request,'projects/delete_template.html',context)



def internships(request):
    internships = Internship.objects.all()
    context ={ 'internships': internships}
    return render(request,'internships/internships.html',context)

def internship(request, pk):
    internshipObj = Internship.objects.get(id=pk)
   
    print('internshipObj:',internshipObj)
    return render(request,'internships/single-internship.html',{'internship':internshipObj})


def createinternship(request):
    form = internshipForm()
    if request.method == 'POST':
        form = internshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "internships/internship_form.html",context )
