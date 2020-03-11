from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

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

def user_login(request):

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = authenticate(username=email,password=password)

		if user:
			if user.is_active :
				login(request)
				return HttpResponseRedirect(reverse('blog:feed'))

			else:
				return HttpResponse("Account not active. ")

		else:
			return HttpResponse("Invalid login details.Please Sign Up ")

	else:
		return render(request,'blog/home.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))