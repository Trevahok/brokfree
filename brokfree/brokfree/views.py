from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from registration.models import UserProfile
def home(request):
    if request.user.is_authenticated:
        return(render(request,'home.html'))
    return(render(request,'home.html'))
