from django.shortcuts import render
from .forms import UserRegistration,UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def register_view(request):

	registered = False

	if request.method == 'POST':
		user_form=UserForm(data=request.POST)
		profile_form=UserRegistration(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()
			registered = True

		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserRegistration()

	return render(request,'user_account/register.html',
		{'user_form':user_form,
		  'profile_form':profile_form,
		  'registered':registered
		  })

def home(request):
	return render(request,'blog/home.html')


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(reverse('blog:home'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.info(request, "Logged in successfully!")
                return HttpResponseRedirect(reverse('blog:feed'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user_account/login.html', {})