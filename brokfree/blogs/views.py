from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_list_or_404
from django.contrib.auth.models import User
from .forms import  BlogForm
# Create your views here.
def blogposts(request):
    posts = get_list_or_404(Post)
    blog_form = BlogForm(request.POST or None)
    if blog_form.is_valid():
        post = blog_form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect( 'posts')
    return render(request, 'posts.html', {'posts': posts, 'blogform' : blog_form })
