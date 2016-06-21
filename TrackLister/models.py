from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Tracks(models.Model):
    track_name = models.CharField(max_length=100, blank=False, required=True)
    genre = models.CharField(max_length=50, null=True)
    artist = models.CharField(max_length=100, blank=True, default='')
    release_year = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.track_name == '':
            raise ValidationError('Track name cannot be empty')


class Genres(models.Model):
    genre = models.CharField(max_length=50, blank=False, required=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.genre == '':
            raise ValidationError('Genre name cannot be empty')
