from rest_framework import generics
from serializers import TracksSerialzer, GenreSerializer
from .models import Tracks, Genres


class ListTracks(generics.ListCreateAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerialzer


class ModifyTracks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerialzer


class ListGenres(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class ModifyGenres(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

