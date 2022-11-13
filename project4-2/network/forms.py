from django import forms
from .models import Post
from djangoformsetjs.utils import formset_media_js


class PostForm(forms.ModelForm): 
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':45}), label = '')
    class Meta:
        model = Post
        exclude = ("user_id", "datetime", "likes",)
