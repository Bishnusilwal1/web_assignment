from django.contrib import admin
from cinema.models import Genre, Director, Movie, Cast
# Register your models here.

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Cast)