"""GreedyMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

from GreedyMusic.views import home
from TrackLister.views import tracks, genres, track_detail, genre_detail, search

app_name = 'tracks'
admin.autodiscover()

urlpatterns = [
    # page views
    url(r'^$', home, name='home'),
    url(r'^search/$', search, name='search'),
    url(r'^tracks/$', tracks, name='tracks'),
    url(r'^genres/$', genres, name='genres'),
    url(r'^track/(?P<pk>\w+)/$', track_detail, name='track_detail'),
    url(r'^genre/(?P<pk>\w+)/$', genre_detail, name='genre_detail'),
    url(r'^admin/', admin.site.urls),
]
