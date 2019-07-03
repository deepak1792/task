from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'ObjectAdd/$', csrf_exempt(views.addobject)),
    re_path(r'ObjectView/$', views.getobject),
]
