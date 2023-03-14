from django.shortcuts import render
from .models import Movies


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def films_main(request):
    return render(request, 'main/films.html')


def films_film(request, id):
    movie = Movies.objects.filter(id=id)
    if(movie):
        return render(request, 'main/film.html', movie)
    else:
        return render(request, 'main/404.html')