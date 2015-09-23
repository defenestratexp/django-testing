from django.conf.urls import url
from . import views

urlpatters = [
        #url(r'^(?P<passed_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^$', views.amidata, name='amidata'),
        url(r'^$', views.splash, name='splash'),
        ]

