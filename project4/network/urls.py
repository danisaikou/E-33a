
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"), 
    path("posts", views.AllPostsView.as_view(), name="posts"), 
    path("posts/<int:page>", views.posts, name="posts-per-page"),
    path("posts.json", views.post_api, name="posts-api")
]
