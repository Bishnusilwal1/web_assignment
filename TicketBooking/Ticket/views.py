from django.shortcuts import render, redirect
from django.http import HttpResponse
from cinema.filter import MovieFilter
from accounts.models import Profile
from Ticket.models import Cinema, Show, Ticket
from cinema.models import Movie, Genre, Director, Cast
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from accounts.form import LoginForm
from django.contrib.auth.decorators import login_required

def index(request):
    now_showing_movies = Movie.objects.all()[:4]
    coming_sooon_movies = Movie.objects.all()[:4]
    genre = Genre.objects.filter(movie=now_showing_movies)
    context = {
        'now_showing': now_showing_movies,
        'coming_sooon': coming_sooon_movies,
        'genre': genre,
        }
    return render (request,"ticket/home.html", context)


def cinemas(request):
    context = {}
    return render(request, 'ticket/cinemas.html', context)

def tickets(request):
    context = {}
    return render(request, 'ticket/tickets.html', context)
