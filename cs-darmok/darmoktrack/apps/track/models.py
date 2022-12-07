from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    def __str__(self):
        return self.username

class Project(models.Model):
    project_manager = models.ForeignKey(User, related_name='project_manager', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    start = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=250)

    class Meta: 
        ordering = ['start']

    def __str__(self):
        return self.name

    def registered_time(self):
        return 0

    def tasks_remaining(self):
        return 0 # self.tasks.filter(status=Task.TODO).count()

