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
