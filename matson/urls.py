"""matson URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from matsonamis import urls

urlpatterns = [
        #url(r'^matsonamis', 'matsonamis.views.detail', name='amidetail'),
        #url(r'^amidetail', 'matsonamis.views.amidetail', name='amidetail'),
        #url(r'^amiresults', 'matsonamis.views.amiresults', name='amiresults'),

        # This example is given on the tutorial for django 1.8 but doesn't work
        #url(r'^test/', include('matsonamis.urls')),

        #These urlconfs work just fine
        url(r'^data', 'matsonamis.views.amidata', name='amidata'),
        url(r'^ami', 'matsonamis.views.splash', name='splash'),
        url(r'^admin/', include(admin.site.urls)),
]
