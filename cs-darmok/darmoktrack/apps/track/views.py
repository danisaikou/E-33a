from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta

import json

from .models import User, Project, ProjectTask, TimeModel
from .forms import NewProject, AddTaskForm, UpdateTaskForm, TimeForm


def index(request):
        return render(request, "track/index.html")

def project_list(request):

    return render(request, "track/projects.html", {
            "projects": request.user.project_list.all(),
        })

@login_required
def create_project(request):
    
     # Generate form from model forms for creating a listing, make sure the method is POST
    if request.method == "POST":
        form = NewProject(request.POST)

        # Check that the form is valid before proceeding 
        if form.is_valid():

            # Don't save the form until getting the user information so that it is stored with the listing
            proj = form.save(commit=False)
            proj.projects = request.user
            proj.project_manager = request.user
            
            # Then save it and generate a blank form so the user knows something happened with their input
            proj.save()
            form = NewProject()
    
    # If it's not POST, give the user the form to fill out 
    else: 
        form = NewProject()
    
    # To the listing page with the form 
    return render(request, "track/create_project.html", {
        'form': form
         
    })

class edit_project(UpdateView):
    model = Project
    template_name = "track/edit_project.html"
    fields = ['name', 'budget_hours', 'budget_dollars',]
    def get_success_url(self):
        return reverse('projects')

def project(request, id):
    projects = Project.objects.filter(id=id)
    project = Project.objects.get(id=id)
    time_models = project.time_models.all()
    form = AddTaskForm()
    timeform = TimeForm(initial={'project': project})

    if request.method == "POST":

        form = AddTaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('project', id=id)
        else: 
            form = AddTaskForm()
        
        timeform = TimeForm(request.POST)

        if timeform.is_valid():
            print('Form is valid.')
            time_model = TimeModel(
                start_time=timeform.cleaned_data['start_time'],
                end_time=timeform.cleaned_data['end_time'],
                project_id=id, 
            )
            time_model.save()

            return redirect('project', id=id)
        else: 
            print(timeform.errors)
            messages.error(request, 'everything is terrible but at least we are all going to die')
            timeform = TimeForm()
            #display error message 
    
    tasks_todo = ProjectTask.objects.filter(status=ProjectTask.TODO)
    tasks_complete = ProjectTask.objects.filter(status=ProjectTask.COMPLETE)
    tasks_canceled = ProjectTask.objects.filter(status=ProjectTask.CANCELED)
    elapsed_time = project.get_elapsed_time()

    return render(request, "track/project.html", {
        "projects": projects, 
        "id": id, 
        "tasks_todo": tasks_todo, 
        "tasks_complete": tasks_complete, 
        "tasks_canceled": tasks_canceled,
        "form": form,
        "timeform": timeform, 
        "project": project, 
        "time_models": time_models,
        "elapsed_time": elapsed_time,
    })


def view_tasks(request):
    tasks = ProjectTask.objects.all()
    return render(request, 'track/tasks.html', {'tasks': tasks})

def view_task(request, pk): 
    task = ProjectTask.objects.get(pk=pk)
    return render(request, "tasks/task.html", {"task": task})

def update_task(request, pk):
    task = ProjectTask.objects.get(pk=pk)

    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = UpdateTaskForm(instance=task)

    return render(request, 'track/update_task.html', {'form': form})

def update_time(request):
    # get instance to update
    time_model = TimeModel.objects.get(id=1)

    # update start and end fields 
    time_model.start_time = request.POST['start_time']
    time_model.end_time = request.POST['end_time']

    # save 
    time_model.save()
    return HttpResponseRedirect(reverse('projects'))





# def update_timeclock(request):
#     if request.method == "POST": 
#         # process form 
#         timeform = TimeForm(request.POST)
#         if timeform.is_valid():
#             TimeModel = timeform.save()
#             # get start and end time 
#             start_time = TimeModel.start_time
#             end_time = TimeModel.end_time
#             elapsed_time = end_time - start_time

#             # convert to seconds 
#             elapsed_time_seconds = elapsed_time.total_seconds()

#             # update model with time
#             TimeModel.elapsed_time = elapsed_time_seconds
#             TimeModel.save()

#             return HttpResponseRedirect('projects')
         
#         else: 
#             # display form
#             timeform = TimeForm()
#             return render(request, '/track/project.html', {'timeform': timeform})




# Everything below this adapted from previous assignments 
def login_view(request):
    if request.method == 'POST':

        # Attempt sign in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'track/login.html', {
                'message': 'Invalid username and/or password.'
            })
    else:
        return render(request, 'track/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'track/register.html', {
                'message': 'Passwords must match.'
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'track/register.html', {
                'message': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'track/register.html')
