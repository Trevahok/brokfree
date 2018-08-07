from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_list_or_404
# Create your views here.
def blogposts(request):
    posts = get_list_or_404(Post)
    return render(request, 'posts.html', {'posts': posts})
