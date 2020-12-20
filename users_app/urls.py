from django.urls import path
from . import views
	
urlpatterns = [
		path('', views.users_home),
		path('users_add', views.users_add),
	]
