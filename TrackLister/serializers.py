from rest_framework import serializers
from .models import Tracks, Genres


class TracksSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tracks


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres