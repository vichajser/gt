from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
    url(r'^index$', views.index, name='index'),
    url(r'^getData$', views.getData, name='getData'),
)