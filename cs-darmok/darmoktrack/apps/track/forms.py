from django import forms
from .models import Project

class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        fields =('customer', 'name')
        labels = {
            'name': ('Project Name'),
            'customer': ('Customer Name')
        }