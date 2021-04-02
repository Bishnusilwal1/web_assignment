import django_filters
from cinema.models import Movie

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
<<<<<<< HEAD
        fields = ['name']
=======
<<<<<<< HEAD:cinema/filter.py
        fields = ['name',]
=======
        fields = ['name']

        
>>>>>>> 3338aa60c56689aa9e0b2b4302d550cf2d0123d9:Ticket/fliter.py
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
