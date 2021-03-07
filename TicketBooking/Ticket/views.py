from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre

def index(request):
    movies = Genre.objects.all()
    context = {'movies': movies}
    return render  (request,"ticket/home.html", context)

def login_page(request):
    context = {}
    return render(request, 'ticket/login.html', context)

def reg_page(request):
    context = {}
    return render(request, 'ticket/register.html', context)