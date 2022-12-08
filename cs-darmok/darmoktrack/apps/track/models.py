from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import date

class User(AbstractUser):
    def __str__(self):
        return self.username

class Project(models.Model):
    project_manager = models.ForeignKey(User, related_name='project_manager', on_delete=models.CASCADE)
    name = models.CharField("Project Name", max_length=250)
    start = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=250)
    budget_hours = models.IntegerField(default=0)
    budget_dollars = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    is_active = models.BooleanField("Active", default=True)
    projects = models.ForeignKey(User, blank=True, related_name="project_list", on_delete=models.CASCADE)

    class Meta: 
        ordering = ['-start']

    def __str__(self):
        return f"Project {self.id} - {self.name} managed by {self.project_manager.username} with {self.time_spent} elapsed"
    
    def inactive(self):
        if self.is_active():
            return True
        else: 
            return False

def default_future():
        return timezone.now() + timezone.timedelta(days=7)

class TimeClock(models.Model):
    elapsed_time = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class ProjectTask(models.Model):
    #Status Options
    TODO = 'todo'
    COMPLETE = 'complete'
    CANCELED = 'canceled'
    
    CHOICES_STATUS = {
        (TODO, 'todo'),
        (COMPLETE, 'complete'),
        (CANCELED, 'canceled'),
    }

    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    description = models.CharField("Task Description", max_length=250)
    task_owner = models.ForeignKey(User, related_name='task_owner', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=TODO)
    due_date = models.DateTimeField(default=default_future)
    

    class Meta:
        ordering = ['due_date']
    
    def __str__(self):
        return f"{self.description}: due {self.due_date}"

    @property 
    def is_past_due(self):
        return date.today() > {self.due_date}


    


