from django.conf.urls import url, patterns
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^showOne/$', views.showOne),
	url(r'^clear/$', views.clear)
]

