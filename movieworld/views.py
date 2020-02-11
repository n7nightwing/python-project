from django.shortcuts import render, redirect
from .forms import DirectorForm, MovieForm

# Create your views here.
def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            director = form.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm()
    return render(request, 'movieworld/director_form.html', {'form': form})
