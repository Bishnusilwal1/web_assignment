from django.shortcuts import render, redirect
from cinema.models import Movie
<<<<<<< HEAD
from accounts.models import Profile
=======
<<<<<<< HEAD
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
from Ticket.models import Show, Ticket
from django.contrib.auth.models import User
from .forms import ShowForm
from django.views.decorators.csrf import csrf_protect
from myadmin.forms import AdminLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only

@csrf_protect
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = AdminLoginForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(request, username=data['username'], password=data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return render(request, 'admin1/adlogin.html', {'form': form})
        form = AdminLoginForm
        return render(request, 'admin1/adlogin.html', {'form': form})

@login_required
@csrf_protect
def admin_logout(request):
    logout(request)
    return redirect('adlogin')

"""
    function for theatre
"""
@admin_only
<<<<<<< HEAD
@login_required
=======
=======
from accounts.models import Profile
from Ticket.models import Show, Ticket
from django.contrib.auth.models import User
from .forms import ShowForm
from django.views.decorators.csrf import csrf_protect
from myadmin.forms import AdminForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
"""
    function for theatre
"""

@login_required
>>>>>>> 3338aa60c56689aa9e0b2b4302d550cf2d0123d9
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
def home(request):
    theatre = Show.objects.count()
    movies = Movie.objects.count()
    users = User.objects.count()
    bookings = Ticket.objects.count()
    context = {
        'theatre': theatre,
        'movies': movies,
        'users': users,
        'bookings': bookings
    }
    return render(request, 'admin1/dashboard.html', context)

def theatre(request):
    theatre = Show.objects.all()
    context = {
        'theatres': theatre
    }
    return render(request, 'admin1/theatre.html', context)

@csrf_protect
def theatre_add(request):
    form = ShowForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'admin1/addTheatre.html', context)

def theatre_edit(request, tid):
    theatre = Show.objects.get(id=tid)
    form = ShowForm(request.POST or None, instance=movie)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'theatre':theatre,
        'form': form
        }
    return render(request, 'admin1/addTheatre.html', context)

def theatre_delete(request, tid):
    theatre = Show.objects.get(id=tid)
    theatre.delete()
    return redirect('/')


"""
    Function for movies
"""
def movie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'admin1/movies-dashboard.html', context)

@csrf_protect
def movie_add(request):
    form = ShowForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'admin1/addmovie.html', context)

def movie_edit(request, tid):
    movie = Show.objects.get(id=tid)
    form = ShowForm(request.POST or None, instance=movie)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'movie':movie,
        'form': form
        }
    return render(request, 'admin1/addmovie.html', context)

def movie_delete(request, tid):
    movie = Show.objects.get(id=tid)
    movie.delete()
    return redirect('/')



    """
    Function for shows
"""
def show(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'admin1/dashboard.html', context)

@csrf_protect
def show_add(request):
    form = ShowForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'admin1/addmovie.html', context)

def show_edit(request, tid):
    movie = Show.objects.get(id=tid)
    form = ShowForm(request.POST or None, instance=movie)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'movie':movie,
        'form': form
        }
    return render(request, 'admin1/addmovie.html', context)

def show_delete(request, tid):
    movie = Show.objects.get(id=tid)
    movie.delete()
    return redirect('/')


def users(request):
    user = Profile.objects.all()
    context = {
        'user':user
    }
    return render(request, 'admin1/user-dash.html', context)


#admin login form


def admin_login(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "logged on")
                return redirect("admin-home")
            else:
                messages.add_message(request, messages.ERROR, "username or password is incorrect")
                return render(request, 'admin1/login.html', {'form': form})
    form = AdminForm
    context={
        'form':form,
    }
    return render(request, 'admin1/login.html',context)

def admin_logout(request):
    logout(request)
    return redirect('admin-login')


    