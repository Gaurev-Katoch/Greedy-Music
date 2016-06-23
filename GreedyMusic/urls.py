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
from TrackLister.views import tracks, genres, track_detail
from TrackLister.apis import ListTracks, ModifyTracks, ListGenres, ModifyGenres

app_name = 'tracks'
admin.autodiscover()

urlpatterns = [
    # page views
    url(r'^tracks/$', tracks, name='tracks'),
    url(r'^genres/$', genres, name='genres'),
    url(r'^track/(?P<pk>\w+)/$', track_detail, name='detail'),
    url(r'^admin/', admin.site.urls),

    # api views
    url(r'^api/list_tracks/$', ListTracks.as_view(), name='tracks_list'),
    url(r'^api/mod_track/(?P<pk>\w+)/$', ModifyTracks.as_view(), name='track_detail'),
    url(r'^api/list_genres/$', ListGenres.as_view(), name='genres_list'),
    url(r'^api/mod_genre/(?P<pk>\w+)/$', ModifyGenres.as_view(), name='genre_detail'),
]
