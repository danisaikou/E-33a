from django.contrib import admin

from .models import User, Project, ProjectTask, TimeClock, TimeModel

# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('get_elapsed_time', )

admin.site.register(User)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTask)
admin.site.register(TimeClock)
admin.site.register(TimeModel)