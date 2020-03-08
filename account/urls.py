from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url,include



urlpatterns = [
	url(r'^$',views.register_view,name='register'),
]
