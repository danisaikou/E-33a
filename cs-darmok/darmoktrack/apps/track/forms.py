from django import forms
from django.forms import Select
from .models import Project, ProjectTask, TimeModel, Expense

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

class ExpenseForm (forms.ModelForm):
    class Meta: 
        model = Expense
        fields = ('project', 'amount', 'description', 'date',)
        labels = {
            'project': ('Project'), 
            'description': ('Description'), 
            'amount': ('Amount'), 
            'date': ('Date Incurred'),
        }
        widgets = {
            'project': Select(),
        }

class TimeForm(forms.ModelForm):
    class Meta:
        model = TimeModel
        fields = ('start_time', 'end_time', 'project', )
        widgets = {
            'start_time': forms.TextInput(attrs={'id': 'start_time'}),
            'end_time': forms.TextInput(attrs={'id': 'end_time'}),
            'project': Select(),
        }
    project = forms.ModelChoiceField(queryset=Project.objects.all())
  