from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import success, error, info

from .models import User, Post
from .forms import PostForm

#class AllPostsView(ListView):
#    paginate_by = 10
#    model = Post


def index(request):
    # Paginating
    posts = Post.objects.all().order_by('-datetime')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
       
    return render(request, "index.html", {
        "posts": page_obj,
        "create_post": PostForm(),
        "page_obj": page_obj,
        "page_number": page_number,
    }) 

@login_required
def create_post(request):

    if request.method == "POST":
        id = request.POST.get("id")
        create_post = request.POST.get("post")
        if len(create_post) is not 0: 
            post = Post.objects.get(id=id)
            post.user_id == request.user_id
            post.post = create_post()
            post.save()
        return JsonResponse({
            "post_id": post.id,
            "username": request.user_id,
            "datetime": post.datetime()
        })
    return JsonResponse({})
                


   
@login_required
def edit_posts(request):
    if request.method == "POST":
        id = request.POST.get("id")
        create_post = request.POST.get("post")
        try: 
            post = Post.objects.get(id=id)
            if post.user == request.user:
                post.post = create_post.strip()
                post.save()
                return JsonResponse({})
        except: 
            return JsonResponse({})
    return JsonResponse({})


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

@login_required
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
