from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^zc/', views.zc),
    url(r'dl/', views.dl),
    url(r'login/', views.login),
]