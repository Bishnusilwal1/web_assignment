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
from Ticket.forms import TicketForm
from django.contrib import messages
from Ticket.models import Ticket
from cinema.models import Movie
from django.views.generic import ListView
# from accounts.auth import allowed_user

# @allowed_user(['users'])
def cinemas(request):
    movie = Movie.objects.all()[:4]
    cinema = Cinema.objects.all()
    context = {
        'cinema': cinema,
        'movie': movie,
        'activate_cinema': 'active',
    }
    return render(request, 'ticket/cinemas.html', context)

@login_required(login_url="login")
def tickets(request):
    inst_user = request.user
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.ticket_user = inst_user
            instance.save()
            messages.add_message(request, messages.SUCCESS, "TIcket added successfully")
            return redirect('ticket_form')
        else:
            messages.add_message(request, messages.ERROR, "Couldnot buy ticket")
            return render(request, 'tickets/ticket_form.html', {'form':form})
    context = {
        'form':  TicketForm(),
        'activate_ticket': 'active'
    }
    print(context)
    return render(request, 'tickets/ticket_form.html', context)

@login_required(login_url="login")
def ticket_lists(request):
    user = request.user
    ticket = Ticket.objects.filter(ticket_user=user)
    context = {
        'ticket': ticket
    }
    return render(request, 'tickets/ticket_list.html', context)

# class MovieSearch(ListView):
#     model = Movie
#     template_name = "ticket/search_list.html"

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         data = Movie.objects.filter(
#             Q(name__icontains=query)
#         )
#         return data

def search_query(request):
    query = Movie.objects.filter(name="bishnu vai")
    filter = MovieFilter(request.GET, queryset=query)
    context = {
        'filter': filter
    }
    return render(request, 'ticket/search_list.html', context)
 