from django.db import models
from django.contrib.auth.models import User
'''class Post(models.Model):
	"""docstring for Post"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted=models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
	'''
class Account(models.Model):
	firstname = models.CharField(max_length=50,default=' ')
	lastname = models.CharField(max_length=50,default=' ')
	email = models.EmailField(verbose_name="email",max_length=60,unique=True,default=' ')
	#birthday = models.DateField(default=YYYY-MM-DD)
	gender= models.CharField(max_length=50,default=' ')

	def __str__(self):
		return self.email
	
# Create your models here.
