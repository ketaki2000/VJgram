from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request,'blog/home.html')
	
def about(request):
	return render(request,'blog/aboutus.html')

def welcome(request):
	return render(request,'blog/welcome.html')

@login_required
def login(request):
	return render(request,'blog/feed.html')
