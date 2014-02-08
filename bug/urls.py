from django.conf.urls import patterns, url

from bug import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^list$', views.list, name='list'),
	url(r'^add$', views.add, name='add')
)