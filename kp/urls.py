from django.conf.urls import patterns, url;
from kp import views;

urlpatterns = patterns('',
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
)