from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView


from .models import User, Post
from .forms import PostForm


def index(request):
    # Pagination
        posts = Post.objects.all().order_by('-datetime')
        paginator = Paginator(posts, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        # Form stuff
        form = PostForm(request.POST or None)

        return render(request, "network/index.html", {
            "posts": posts,
            "form": form, 
            "page_obj": page_obj, 
            "page_number": page_number, 
        })

def post(request):
        form = PostForm(request.POST or None)

        # Confirm validity before proceeding
        if form.is_valid:
            post.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['content']
            form = PostForm()
            return redirect('index')
        
        context = {'form':form, 'text':text}
        return render(request, 'network/index.html', context)
        


# Everything below this was pre-populated, not created by me
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
