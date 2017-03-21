from django.conf.urls import url

from . import views

app_name = 'comments'

urlpatterns = [
    url(r'^(?P<post_id>[0-9]+)/$', views.add, name='add'),
]