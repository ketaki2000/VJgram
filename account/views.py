from django.shortcuts import render
from .forms import UserRegistration
# Create your views here.
def register_view(request):

	form = UserRegistration()
	if request.method == 'POST':
		form=UserRegistration(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return home(request)
		else:
			print('Error')

	return render(request,'account/register.html',{'form':form})

def home(request):
	return render(request,'blog/home.html')