from django.conf.urls import url
from . import views

urlpatters = [
        url(r'^$', views.buildami, name='buildami'),
        url(r'^$', views.amidata, name='amidata'),
        url(r'^$', views.testview, name='testview'),
        url(r'^$', views.splash, name='splash'),
        ]

