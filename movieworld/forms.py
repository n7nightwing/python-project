from django import forms
from .models import Director, Movie

class DirectorForm(forms.ModelForm):

    class Meta:
        model = Director
        fields = ('name', 'nationality', 'birthday',)

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('name', 'genre', 'release_date', 'director_name', 'stars',)