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
	user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
	GENDER = (("1","Male"),("2","Female"))
	firstname = models.CharField(max_length=50,default=' ')
	lastname = models.CharField(max_length=50,default=' ')
	gender= models.CharField(max_length=50,choices=GENDER)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True)

	def __str__(self):
		return self.user.username
	
# Create your models here.
