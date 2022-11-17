
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_post", views.create_post, name="create_post"),
    path("article/edit/<int:id>", views.edit_post, name="edit_post"),
    path("like/", views.like), 
    #path("following/", views.follow, name="following"),
    path('profile/', views.profile, name='profile'),
]
