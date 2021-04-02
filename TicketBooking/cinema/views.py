from django.shortcuts import render
from cinema.models import Movie, Genre, Cast
from django.views.generic import ListView
from cinema.filter import MovieFilter

def index(request):
    now_showing_movies = Movie.objects.all()[:4]
    coming_sooon_movies = Movie.objects.all()[:4]
    context = {
        'now_showing': now_showing_movies,
        'coming_sooon': coming_sooon_movies,
        }
    return render (request,"ticket/home.html", context)


def movie_details(request, mid):
    movie = Movie.objects.get(id=mid)
    genre = Genre.objects.filter(movie=movie)
    cast = Cast.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'genre': genre,
        'cast': cast
        }
    return render(request, 'ticket/movie_details.html', context)

<<<<<<< HEAD
=======
<<<<<<< HEAD
def search_movie(request):
    movie = Movie.objects.all()
    movie_filter = MovieFilter(request.GET, queryset=movie)
    context = {
        'movie_filter': movie_filter,
    }
    return render(request, 'ticket/home.html', context)
=======
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
def search_view(request):
    filter = MovieFilter(request.GET, queryset= Movie.objects.all())
    return render(request, 'ticket/search_list.html', {'filter': filter})


<<<<<<< HEAD
=======
>>>>>>> 3338aa60c56689aa9e0b2b4302d550cf2d0123d9
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
