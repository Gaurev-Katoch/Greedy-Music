from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def tracks(request):
    return HttpResponse("Listing Tracks Here")


def genres(request):
    return HttpResponse("Listing Genres Here")
