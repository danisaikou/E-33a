
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_post", views.create_post, name="create_post"),
    path("post/edit/<int:pk>", views.edit_post.as_view(), name="edit_post"),
    path("profile/edit/<int:pk>", views.edit_profile.as_view(), name="edit_profile"),
    path("like/<int:pk>", views.like, name="like_post"), 
    path('profile/<int:pk>', views.profile, name='profile'),
    path('following/', views.following, name="following"), 
    path("profile/<str:id>/follow", views.follow, name="follow"),

]
