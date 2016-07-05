from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Genres(models.Model):
    genre = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return "%s" % self.genre


def get_rating_list():
    rating_list = []
    for x in range(6):
        rating_list.append((str(x), str(x)))
    return rating_list


class Tracks(models.Model):
    track_name = models.CharField(max_length=100, blank=False, null=False)
    artist = models.CharField(max_length=100, blank=True)
    album = models.CharField(max_length=100, blank=True)
    genres = models.ManyToManyField(Genres, blank=True)
    rating = models.CharField(choices=get_rating_list(), blank=True, max_length=1, null=True)

    def __str__(self):
        return "%s  %s  %s  %s" % (
            self.track_name,
            self.artist,
            self.album,
            self.genres,
        )
