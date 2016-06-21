from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Tracks(models.Model):
    track_name = models.CharField(max_length=100, blank=False)
    genre = models.CharField(max_length=50, null=True, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.track_name == '':
            raise ValidationError('Track name cannot be empty')


class Genres(models.Model):
    genre = models.CharField(max_length=50, blank=False)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.genre == '':
            raise ValidationError('Genre name cannot be empty')
