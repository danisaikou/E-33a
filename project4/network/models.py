from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def __str__(self):
        return self.username

class Post(models.Model):
    user_id = models.ForeignKey(User, verbose_name="user_id", on_delete=models.CASCADE)
    content = models.TextField("content", max_length=260)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"posted by {self.user_id} on {self.datetime}"
    