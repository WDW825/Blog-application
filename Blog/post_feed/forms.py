from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'post_date', 'post_text')

#TODO: author name must be taken from session