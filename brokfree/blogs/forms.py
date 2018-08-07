from .models import Post
from django import forms

class BlogForm(forms.Form):
    class Meta:
        model = Post
        exclude = '__all__'
        fields = ['desc' , 'content' ,'likes' ,'bhk']
