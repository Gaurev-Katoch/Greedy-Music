from django import forms
from .models import Tracks, Genres


class TrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = '__all__'
    genres = forms.ModelMultipleChoiceField(queryset=Genres.objects.all())


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = '__all__'
