from django import forms
from .models import  Movie, Director

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('name', 'genre', 'release_date', 'director', 'synopsis', 'photo_url',)

class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ('director_name', 'nationality', 'birthday', 'bio', 'photo_url',)

