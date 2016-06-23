from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.serializers import serialize
from django.template import loader
from models import Tracks, Genres
from apis import ListTracks, ModifyTracks, ListGenres, ModifyGenres
# Create your views here.


def tracks(request):

    # track_list = serialize("json", Tracks.objects.all())
    track_list = ListTracks.as_view()(request).data
    template = 'tracks.html'
    context = {'track_list': track_list, }

    return render(request, template, context)


def track_detail(request, pk):

    # try:
    #     track = Tracks.objects.get(id=pk)
    # except:
    #     return HttpResponse('Track Not Found')
    template = 'track.html'
    track = ModifyTracks.as_view()(request, pk=pk).data
    context = {'track': track, }

    return render(request, template, context)

def genres(request):
    return HttpResponse(Genres.objects.all())
