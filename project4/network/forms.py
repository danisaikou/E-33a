from django.forms import ModelForm
from .models import Post as PostModel

class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content']
