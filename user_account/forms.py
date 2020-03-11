from django import forms
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegistration(forms.ModelForm):
	class Meta:
		model = Account
		fields = ('firstname','lastname','gender','profile_pic')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','password','email')