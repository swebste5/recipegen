from . import views
#from django.conf.urls import patterns, include, urllib
import django.conf.urls
from django.conf.urls import url, include

app_name = "recipe"
urlpatterns = [
#ex: /form to add new recipe
	url(r'^$', views.index, name='index'),
 	url(r'^add/$', views.add, name='add'),
	url(r'^newRecipe/$', views.newRecipe, name='newRecipe'),
	url(r'^retrieve/$', views.retrieve, name='retrieve'),
	url(r'^retrieveRecipe/$', views.retrieveRecipe, name='retrieveRecipe'),
	url(r'^delete/$', views.delete, name='delete'),
	url(r'^deleteRecipe/$', views.deleteRecipe, name='deleteRecipe')
]
