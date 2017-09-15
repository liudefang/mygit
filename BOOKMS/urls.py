"""BOOKMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from bookapp import reader.views
admin.autodiscover()
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^regist/$', views.regist),

    url(r'^index/$', 'reader.views.index', name="readers_index"),
    url(r'^add/$', 'reader.views.addReader', name="readers_add"),
    url(r'^edit/(?P<id>\d+)/$', 'reader.views.editReader', name="readers_edit"),
    url(r'^delete/(?P<id>\d+)/$', 'reader.views.delReader', name="readers_delete"),
    url(r'^selecteddelete/$', 'reader.views.selecteddelReader', name="readers_selecteddelete"),
    url(r'^search/$', 'reader.views.searchReader', name="readers_search"),
]