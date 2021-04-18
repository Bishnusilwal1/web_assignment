from django.shortcuts import render
from cinema.models import Movie, Genre, Cast
from django.views.generic import ListView
from cinema.filter import MovieFilter

def index(request):
    now_showing_movies = Movie.objects.all()[:4]
    coming_sooon_movies = Movie.objects.all()[:4]
    movie = Movie.objects.all()
    movie_filter = MovieFilter(request.GET, queryset=movie)
    movie_qs = movie_filter.qs
    context = {
        'now_showing': now_showing_movies,
        'coming_sooon': coming_sooon_movies,
        'movie_filter': movie_filter,
        'movie_qs': movie_qs,
        'activate_home': 'active'
        }
    return render (request,"ticket/home.html", context)


def movie_details(request, mid):
    movie = Movie.objects.get(id=mid)
    genre = Genre.objects.filter(movie=movie)
    cast = Cast.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'genre': genre,
        'cast': cast,
        }
    return render(request, 'ticket/movie_details.html', context)


def search_view(request,):
    movie = Movie.objects.all()
    movie_filter = MovieFilter(request.GET, queryset=movie)
    movie_qs = movie_filter.qs
    context = {
        'movie_filter': movie_filter,
        'movie_qs': movie_qs
    }
    return render(request, 'ticket/search_list.html', context)
