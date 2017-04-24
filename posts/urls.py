from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^tag/(?P<tag>[-\w]+)/$', views.tag, name='tag'),
    url(r'^post/new$', views.new, name='new'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.detail, name='detail'),
	url(r'^$', views.index, name = 'index'),
]