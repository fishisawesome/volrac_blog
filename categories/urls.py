from django.conf.urls import url

from . import views

app_name = 'categories'

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.category, name='detail'),
]