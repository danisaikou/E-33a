from django.forms import ModelForm
from .models import Posts as PostModel

class PostForm(ModelForm):
    model = PostModel
    fields = ['title', 'content']



    