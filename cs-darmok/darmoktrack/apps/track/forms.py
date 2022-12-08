from django import forms
from .models import Project, ProjectTask

class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields =('customer', 'name', 'budget_hours', 'budget_dollars')
        labels = {
            'name': ('Project Name'),
            'customer': ('Customer Name'), 
            'budget_hours': ('Estimated Hours'),
            'budget_dollars': ('Budget'),

        }

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = ProjectTask
        fields =('project', 'description', 'task_owner', 'due_date',)
        labels = {
            'project': ('Project'),
            'description': ('Task Description'),
            'task_owner': ('Responsible'),
            'due_date': ('Due Date'),
        }
    
    