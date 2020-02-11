from django.shortcuts import render, redirect

from .models import Movie, Director
from .forms import DirectorForm, MovieForm


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})

def director_list(request):
    directors = Director.objects.all()
    return render(request, 'movieworld/director_list.html', {'directors': directors})