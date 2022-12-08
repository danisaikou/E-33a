from django.contrib import admin

from .models import User, Project, ProjectTask, TimeClock

# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(ProjectTask)
admin.site.register(TimeClock)