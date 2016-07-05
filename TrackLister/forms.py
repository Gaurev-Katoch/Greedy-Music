from django import forms
from .models import Tracks


class TrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        exclude = ['genres']
