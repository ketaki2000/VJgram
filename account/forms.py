from django import forms
from .models import Account

class UserRegistration(forms.ModelForm):
	class Meta:
		model = Account
		fields = '__all__'