
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url,include

app_name = "blog"

urlpatterns = [
   # path('', views.home,name='blog-home'),
   url(r'^$',views.home,name='home'),
    path('about/', views.about,name='blog-about'),
    path('welcome.html/', views.welcome,name='welcome'),
    path('aboutus.html/', views.about,name='about'),
    path('feed.html/', views.login,name='feed'),
   
]
