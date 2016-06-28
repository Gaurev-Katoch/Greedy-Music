from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.serializers import serialize
from django.template import loader
from models import Tracks, Genres
from apis import ListTracks, ModifyTracks, ListGenres, ModifyGenres
from forms import TrackForm, GenreForm
# Create your views here.


def tracks(request):

    # track_list = serialize("json", Tracks.objects.all())
    track_list = ListTracks.as_view()(request).data
    template = 'tracks.html'
    context = {'track_list': track_list, }

    return render(request, template, context)


def track_detail(request, pk):

    # try:
    #     track = Tracks.objects.filter(id=pk).values()
    # except:
    #     return HttpResponse('Track Not Found')
    template = 'track.html'
    # track = ModifyTracks.as_view()(request, pk=pk).data
    #
    if request.method == 'POST':
        update_dict = request.POST.dict()
        if update_dict.get('csrfmiddlewaretoken'):
            update_dict.pop('csrfmiddlewaretoken')
        for item in update_dict.items():
            print item
            print update_dict[item]
            if update_dict[item] == u'':
                update_dict.pop(item)

        if pk == 0:
            ob = Tracks.object.create(**update_dict)
        else:
            ob = Tracks.objects.filter(id=pk).update(**update_dict)
            if ob == 1:
                ob = Tracks.objects.filter(id=pk).values()[0]
            else:
                ob = {}
        if ob:
            id = ob['id']
        else:
            id = 0
        form = TrackForm(ob)
    else:
        try:
            f = Tracks.objects.filter(id=pk).values()[0]
            id = f['id']
            form = TrackForm(f)
        # print f
        except Exception as e:
            print e
            form = TrackForm()
            id = 0
    # print form
    print id
    context = {'form': form, 'id': id, }
    # print f
    return render(request, template, context)


def genres(request):
    return HttpResponse(Genres.objects.all())
