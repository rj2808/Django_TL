
from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    )

