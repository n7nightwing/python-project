from django import forms
from .models import  Movie. Director

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('name', 'genre', 'release_date', 'director_name', 'stars', 'photo_url',)

class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ('name', 'nationality', 'birthday', 'bio', 'movies' 'photo_url',)

