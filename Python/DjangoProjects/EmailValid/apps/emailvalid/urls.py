from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^back$', views.goback),
]
