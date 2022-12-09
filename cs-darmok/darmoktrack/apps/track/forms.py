from django import forms
from .models import Project, ProjectTask, TimeModel

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

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = ProjectTask
        fields =('description', 'task_owner', 'status')

class TimeForm(forms.ModelForm):
    class Meta:
        model = TimeModel
        fields = ('start_time', 'end_time', )
        widgets = {
            'start_time': forms.TextInput(attrs={'id': 'start_time'}),
            'end_time': forms.TextInput(attrs={'id': 'end_time'}),
        }
    project = forms.ModelChoiceField(queryset=Project.objects.all())
  