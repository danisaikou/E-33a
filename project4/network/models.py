from datetime import datetime
from email import contentmanager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField('self', blank=True, related_name="following")
    pass
   
    def __str__(self) -> str:
        return self.username

class Posts():
    user_id = models.ForeignKey("app.Model", verbose_name=("user_id"), on_delete=models.CASCADE)
    title = models.CharField("title", max_length=150)
    content = models.TextField("content", max_length=260)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.title} by {self.user_id} on {self.datetime}"