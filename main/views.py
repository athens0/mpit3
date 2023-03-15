from django.shortcuts import render
from .models import Movies


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def films_main(request):
    return render(request, 'main/films.html')


def films_film(request, id):
    if(Movies.objects.filter(id=id)):
        movie = Movies.objects.get(pk=id)
        data = {
            'title': movie.name,
            'date': movie.publish_date,
            'dur': movie.duration,
            'age': movie.pg,
            'author': movie.author,
            'scenarist': movie.scenarist,
            'stars': movie.stars,
            'description': movie.description,
            'rates_count': movie.rates_count,
            'rates_sum': movie.rates_sum,
            'trailer_url': movie.trailer_url,
            'poster_url': movie.poster_url,
        }
        if(movie.rates_count == 0):
            data['rate'] = '-'
        else:
            data['rate'] = movie.rates_sum / movie.rates_count
        return render(request, 'main/film.html', data)
    else:
        return render(request, 'main/404.html')
    
    
def subscription(request):
    return render(request, 'main/subscription.html')


def docs(request):
    return render(request, 'main/docs.html')