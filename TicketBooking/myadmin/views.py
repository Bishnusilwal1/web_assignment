











from django.shortcuts import render, redirect
from cinema.models import Movie,Cast,Genre,Director
from accounts.models import Profile
from Ticket.models import Show, Ticket
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from myadmin.forms import AdminLoginForm, ShowForm,MovieForm,UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from cinema.forms import CastForm,GenreForm,DirectorForm

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

@login_required(login_url="adlogin")
@csrf_protect
def admin_logout(request):
    logout(request)
    return redirect('adlogin')

@login_required(login_url="adlogin")
@admin_only
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

    
""" theatre """

def theatre(request):
    theatre = Show.objects.all()
    context = {
        'theatres': theatre,
        
    }
    return render(request, 'admin1/theatre.html', context)

@csrf_protect
def theatre_add(request):
    form = ShowForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'admin1/addTheatre.html', context)

def update_theatre(request,tid):
    show=Show.objects.get(id=tid)
    if request.method=='POST':
        show.name=request.POST['name']
        show.show_start_time=request.POST['show_start_time']
        show.show_end_time=request.POST['show_end_time']
        show.status=request.POST['status']
        show.price=request.POST['price']
        show.save()
        return redirect('dashboard')
    context={
        'show':show
    }
    return render(request,'admin1/edit_theatre.html',context)


def theatre_delete(request, tid):
    theatre = Show.objects.get(id=tid)
    theatre.delete()
    return redirect('dashboard')


"""  movies  """
def movie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'admin1/movies-dashboard.html', context)

@csrf_protect
def movie_add(request):
    form = MovieForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'admin1/addmovie.html', context)

def edit_movie(request ,id):
    movie=Movie.objects.get(id=id)
    if request.method=='POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('dashboard')
    context={
        'movie':movie,
        'form': MovieForm()
    }
    print(MovieForm())
    return render(request,'admin1/edit_movie.html',context)


def movie_delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('dashboard')


""" users """

def users(request):
    user = User.objects.all()
    context = {
        'user':user
    }
    return render(request, 'admin1/user-dash.html', context)

def ticket_dash(request):
    ticket = Ticket.objects.all()
    context = {
        'ticket':ticket
    }
    return render(request, 'admin1/ticket_dashboard.html', context)


@csrf_protect
def user_add(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'admin1/adduserform.html', context)

def user_edit(request, tid):
    movie = user.objects.get(id=tid)
    form = UserForm(request.POST or None, instance=movie)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'movie':movie,
        'form': form
        }
    return render(request, 'admin1/aduserform.html', context)

def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('dashboard')

def cast(request):
    casts = Cast.objects.all()
    return render(request, 'admin1/cast_dashboard.html', {'casts':casts})

@csrf_protect
def cast_add(request):
    form = CastForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'admin1/addcast.html', context)

def cast_edit(request, tid):
    cast = Cast.objects.get(id=tid)
    form = CastForm(request.POST or None, instance=cast)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'cast':cast,
        'form': form
        }
    return render(request, 'admin1/addcast.html', context)

def cast_delete(request, tid):
    cast = Cast.objects.get(id=tid)
    cast.delete()
    return redirect('dashboard')

    # #delete Ticket



def ticket(request):
    ticket = Ticket.objects.all()
    return render(request, 'admin1/ticket_dashboard.html', {'ticket':ticket})

def ticket_delete(request, cid):
    ticket = Ticket.objects.get(id=cid)
    ticket.delete()
    return redirect('dashboard')












#Directors


def director(request):
    directors = Director.objects.all()
    return render(request, 'admin1/director_dashboard.html', {'directors':directors})

@csrf_protect
def director_add(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': DirectorForm()}
    return render(request, 'admin1/adddirector.html', context)

def director_edit(request, did):
    director = Director.objects.get(id=did)
    form = DirectorForm(request.POST or None, instance=director)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'director':director,
        'form': form
        }
    return render(request, 'admin1/adddirector.html', context)

def director_delete(request, did):
    director = Director.objects.get(id=did)
    director.delete()
    return redirect('dashboard')

#Genre


def genre(request):
    genre = Genre.objects.all()
    return render(request, 'admin1/genre_dashboard.html', {'genre':genre})


@csrf_protect
def genre_add(request):
    form = GenreForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'admin1/addgenre.html', context)

def genre_edit(request, gid):
    genre = Genre.objects.get(id=gid)
    form = GenreForm(request.POST or None, instance=genre)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'genre':genre,
        'form': form
        }
    return render(request, 'admin1/addgenre.html', context)

def genre_delete(request, gid):
    genre = Genre.objects.get(id=gid)
    genre.delete()
    return redirect('dashboard')



