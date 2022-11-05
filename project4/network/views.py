from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import PostForm

from .models import User, Posts

class AllPostsView(ListView, models.Model):
    paginate_by = 10
    model = Posts
    objects = models.Manager()
    

def index(request):
    # !!! paginating the index 
    posts = Posts.objects.all()
    p = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    
    return render(request, "index.html", {
        "page_obj": page_obj
    })

def create_post(request):

    # Generate form from model forms for creating a post, make sure the method is POST (ha)
    if request.method == "POST":
        form = PostForm(request.POST)

        # Check that form is valid before proceeding 
        if form.is_valid():

         # Get user info 
         poster = form.save(commit=False)
         poster.user = request.user

         # Save and generate blank so user knows it worked 
         poster.save()
         form = PostForm()
    
    # If not POST give user form to fill
    else: 
        form = PostForm()
    
    # To the post page with the form 
    return render(request, "network/create_post.html", {
        "form": form
    })

# def post_api(request):
#     page_number = request.GET.get("page", 1)
#     per_page = request.GET.get("per_page", 10)
#     posts = Posts.objects.all()
#     paginator = Paginator(posts, per_page)
#     page_obj = paginator.get_page(page_number)
#     data = [{"title": p.name} for p in page_obj.object_list]

#     payload = {
#         "page": {
#             "current": page_obj.number,
#             "has_next": page_obj.has_next(),
#             "has_previous": page_obj.has_previous(),
#         },
#         "data": data
#     }
#     return JsonResponse(payload)
   

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
