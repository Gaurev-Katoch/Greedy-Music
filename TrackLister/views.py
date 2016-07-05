from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from models import Tracks, Genres
from forms import TrackForm
# Create your views here.


def tracks(request):
    """
    Lists all the tracks
    :param request:
    :return:
    page -- Page no. of paginated data
    """
    pg = int(request.GET.get('page', 1))
    track_list = Tracks.objects.all()
    p = Paginator(track_list, 10)
    if pg > p.num_pages:
        pg = p.num_pages
    obj_list = p.page(pg).object_list

    template = 'tracks.html'
    context = {'track_list': obj_list, 'page_no': pg, 'total_pages': p.num_pages, }

    return render(request, template, context)


def track_detail(request, pk):
    """
    View, Edit and Save details for individual track entries
    :param request:
    :param pk: id of the track in the database
    :return:
    """

    template = 'track.html'
    if request.method == 'POST':
        update_dict = request.POST.dict()
        if update_dict.get('Delete'):
            Tracks.objects.filter(id=pk).delete()
            return redirect('tracks')
        gen_list = request.POST.getlist('genres')
        if update_dict.get('csrfmiddlewaretoken'):
            update_dict.pop('csrfmiddlewaretoken')
        if update_dict.get('genres'):
            update_dict.pop('genres')
        if update_dict['track_name'] != '':
            if pk == '0':
                try:
                    ob = Tracks.objects.create(**update_dict)
                    ob.genres.add(*gen_list)
                    pk = ob.id
                except:
                    pk = 0
            else:
                ob = Tracks.objects.filter(id=pk).update(**update_dict)
                if ob == 1:
                    ob = Tracks.objects.get(id=pk)
                    ob.genres.clear()
                    ob.genres.add(*gen_list)
        return redirect('track_detail', pk=pk)
    else:
        try:
            f = Tracks.objects.filter(id=pk).values()[0]
            id = f['id']
            form = TrackForm(f)
        except:
            form = TrackForm()
            id = pk

    try:
        gen_list = Tracks.objects.get(id=pk).genres.all()
    except:
        gen_list = {}
    # print form
    context = {'form': form, 'id': str(id), 'genre_list': Genres.objects.all(), 'selected_genres': gen_list, }
    return render(request, template, context)


def genres(request):
    """
    Lists all the Genres
    :param request:
    :return:
    """

    genre_list = Genres.objects.all()
    template = 'genres.html'
    context = {'genre_list': genre_list, }

    return render(request, template, context)


def genre_detail(request, pk):
    """
    View, Save and Edit individual genre entries
    :param request:
    :param pk: id of genre in database
    :return:
    """
    template = 'genre.html'
    context = {}
    if request.method == 'GET':
        try:
            genre = Genres.objects.get(id=pk)
        except:
            genre = {}
        artists = filter(None, Tracks.objects.filter(genres__in=[pk]).values_list('artist', flat=True))
        context.update({'genre': genre, 'artists': artists, 'id': pk})
    elif request.method == 'POST':
        update_dict = request.POST.dict()
        if update_dict.get('Delete'):
            Genres.objects.filter(id=pk).delete()
            return redirect('genres')
        if update_dict.get('csrfmiddlewaretoken'):
            update_dict.pop('csrfmiddlewaretoken')
        if update_dict['genre'] != '':
            if pk == '0':
                try:
                    genre = Genres.objects.create(**update_dict)
                    pk = genre.id
                except:
                    pk = 0
            else:
                try:
                    Genres.objects.filter(id=pk).update(**update_dict)
                except:
                    pass
        return redirect('genre_detail', pk=pk)

    return render(request, template, context)


def search(request):
    """
    Search for tracks by name or genre
    :param request:
    lookup -- search string
    search_by -- Parameter according to which tracks will be searched. Ex. track_name, genre etc.
    :return:
    """
    template = 'tracks.html'
    search_by = request.GET.get('search_by')
    if search_by != 'genres':
        search_dict = {search_by + '__icontains': request.GET.get('lookup')}
        tracks_list = Tracks.objects.filter(**search_dict)
    else:
        gen_list = [x.strip() for x in request.GET.get('lookup').split(',')]
        id_list = Genres.objects.filter(genre__in=gen_list).values_list('id', flat=True)
        tracks_list = Tracks.objects.filter(genres__in=id_list).distinct()
    context = {'track_list': tracks_list, 'call': 'search', }
    return render(request, template, context)
