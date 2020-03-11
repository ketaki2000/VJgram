from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user_account'

urlpatterns = [
	url(r'^register/$',views.register_view,name='register'),
	url(r'^login/$',views.user_login,name='login'),

]
