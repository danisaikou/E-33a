from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib import messages

import json

from .models import User, Project
from .forms import NewProject


def index(request):
        return render(request, "track/index.html")

def projects(request):
    return render(request, "track/projects.html")

def create_project(request):
    
    #Generate form from model forms for creating a new project, make sure POST
    if request.method == "POST":
        form = NewProject(request.POST)

        #Confirm form valid before proceeding 
        if form.is_valid():

            #Get user info first
            project = form.save(commit=False)
            project.user = request.user 

            #Save and generate blank so they know it worked
            project.save()
            form = NewProject()

    else: 
        form = NewProject()

    return render(request, "track/create_project.html", {
        'form': form
    })

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
