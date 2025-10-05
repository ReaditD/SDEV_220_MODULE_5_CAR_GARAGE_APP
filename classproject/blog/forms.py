from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        """fields = __all__# brings in everything"""
        fields = ['title', 'author', 'body'] # fields to use
        #widgets = {}