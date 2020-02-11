from django.shortcuts import render, redirect

from .models import Movie, Director
from .forms import DirectorForm, MovieForm


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movieworld/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movieworld/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movieworld/movie_form.html', {'form': form})

def movie_edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movieworld/movie_form.html', {'form': form})

def movie_delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie_list')

def director_list(request):
    directors = Director.objects.all()
    return render(request, 'movieworld/director_list.html', {'directors': directors})

def director_detail(request, pk):
    director = Director.objects.get(id=pk)
    return render(request, 'movieworld/director_detail.html', {'director': director})

def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            director = form.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm()
    return render(request, 'movieworld/director_form.html', {'form': form})

def director_edit(request, pk):
    director = Director.objects.get(pk=pk)
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            director = form.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm(instance=director)
    return render(request, 'movieworld/director_form.html', {'form': form})

def director_delete(request, pk):
    Director.objects.get(id=pk).delete()
    return redirect('director_list')