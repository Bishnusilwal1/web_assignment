import django_filters
from cinema.models import Movie

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = ['name',]

