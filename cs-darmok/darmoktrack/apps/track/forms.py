from django import forms
from .models import Project

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