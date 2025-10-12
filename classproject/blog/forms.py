from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        """fields = __all__# brings in everything"""
        fields = ['title', 'author', 'body'] # fields to use
        #fields2 = ('title', 'text') #second fields2 is form Django Tutorial
        #widgets = {}