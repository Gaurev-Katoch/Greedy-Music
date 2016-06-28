from __future__ import unicode_literals
from django.db import models
from datetime import date


# Create your models here.


class Genres(models.Model):
    genre = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return "%s" % self.genre


def get_rating_list():
    rating_list = []
    for x in range(0, 6):
        rating_list.append((str(x), str(x)))
    return rating_list


class Tracks(models.Model):
    track_name = models.CharField(max_length=100, blank=False)
    artist = models.CharField(max_length=100, blank=True)
    album = models.CharField(max_length=100, blank=True)
    genres = models.CharField(max_length=100, choices=Genres.objects.all().values_list('genre'))
    release_year = models.PositiveIntegerField(blank=True)
    rating = models.CharField(choices=get_rating_list(), blank=True, max_length=1, null=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.release_year > date.today().year:
            raise ValidationError('Release year cannot be after current year')

    def __str__(self):
        return "%s  %s  %s  %s" % (
            self.track_name,
            self.artist,
            self.album,
            self.genres,
        )
