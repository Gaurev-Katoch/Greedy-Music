from __future__ import unicode_literals
from django.db import models
from datetime import date

# Create your models here.


class Tracks(models.Model):
    track_name = models.CharField(max_length=100, blank=False)
    genre = models.CharField(max_length=50, null=True, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    ablum = models.CharField(max_length=100, blank=True)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.rating > 5:
            raise ValidationError('Rating should be between 0 & 5')
        elif self.release_year > date.today().year:
            raise ValidationError('Release year cannot be after current year')


class Genres(models.Model):
    genre = models.CharField(max_length=50, blank=False)
