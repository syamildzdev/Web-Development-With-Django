from django.urls import path
from . import views

urlpatterns =  [
	path('', views.home, name='cafe-home'),
	path('about', views.about, name='cafe-about')
]