from django.shortcuts import render, redirect

from .models import Movie, Director
from .forms import DirectorForm, MovieForm


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})

def director_list(request):
    directors = Director.objects.all()
    return render(request, 'movieworld/director_list.html', {'directors': directors})


def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            director = form.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm()
    return render(request, 'movieworld/director_form.html', {'form': form})