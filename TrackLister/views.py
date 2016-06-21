from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
import json
from models import Tracks, Genres

# Create your views here.


def tracks(request):

    track_list = serialize("json", Tracks.objects.all())
    return HttpResponse(track_list)


def genres(request):
    return HttpResponse(Genres.objects.all())
