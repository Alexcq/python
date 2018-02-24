from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^blog/$', views.index),
    url(r'^blog/(\d+)/$',views.dell),

    url(r'^new/$',views.new),
    url(r'new/(\d+)/$',views.lk),

    url(r'^write/$',views.write),
    url(r'^write/(\d+)/$',views.modify),
]