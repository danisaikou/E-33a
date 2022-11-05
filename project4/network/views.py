from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import PostForm
from django.contrib.auth.decorators import login_required


from .models import User, Posts

class AllPostsView(ListView):
    paginate_by = 10
    model = Posts
    objects = models.Manager()

    

def index(request):
    # Paginating the index 
    posts = Posts.objects.all().order_by('-datetime')
    paginator = Paginator(posts, 10)
    if request.GET.get("page") is not None: 
        try: 
            posts = paginator.page(request.GET.get("page"))
        except: 
            posts = paginator.page(1)
    else: 
        posts = paginator.page(1)
       
    return render(request, "index.html", {
        "posts": posts
    }) 

def create_post(request):

    # Generate form from model forms for creating a post, make sure the method is POST (ha)
    if request.method == "POST":
        post = request.POST.get("post")
        p = Posts()
        p.post = post
        p.user = request.user
        p.save()
        context = {
            "post_id": p.id,
            "username": request.user.username,
            "timestamp": p.datetime,
        }

        return JsonResponse(context)   
    # To the post page with the form 
    return JsonResponse({})

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
   
@login_required
def edit_posts(request):
    if request.method == "POST":
        id = request.POST.get("id")
        create_post = request.POST.get("post")
        try: 
            post = Posts.objects.get(id=id)
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
