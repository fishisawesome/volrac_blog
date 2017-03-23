from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^post/new$', views.new, name='new'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^$', views.index, name = 'index'),
]