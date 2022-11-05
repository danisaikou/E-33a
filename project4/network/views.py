from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import User, Posts

class AllPostsView(ListView):
    paginate_by = 10
    model = Posts


def index(request):
    return render(request, "network/index.html")

def post_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 10)
    # startswith = request.GET.get("startswith", "")
    # posts = Posts.objects.filter(
    #    name__startswith=startswith
    # )
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"title": p.name} for p in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data
    }
    return JsonResponse(payload)

def posts(request): 
   # !!!! trying stuff from lecture prob delete: 
   # Set 10 
   # start = int(request.GET.get("start") or 0)
   # end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts 
   # data = [] 
   # for i in range(start, end + 1):
    #    data.append(f"Post #{i}")
   
    # Return list of posts
    #return JsonResponse({
     #   "posts": data
   # })

    # !!!! instead of class to do the paginate: 
    #post_list = Posts.objects.all().order_by("datetime")
    #paginator = Paginator(post_list, per_page=10)
    #paginator.GET.get_page(page)
    #context = {"page_obj": page_object}
    #return render(request, "/index.html", context)    

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
