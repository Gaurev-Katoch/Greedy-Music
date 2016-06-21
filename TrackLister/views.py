from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.template import loader
from models import Tracks, Genres

# Create your views here.


def tracks(request):

    # track_list = serialize("json", Tracks.objects.all())
    track_list = Tracks.objects.all()
    template = loader.get_template('templates/tracks.html')
    context = {'tracks_list': track_list, }

    return HttpResponse(template.render(context, request))


def genres(request):
    return HttpResponse(Genres.objects.all())
