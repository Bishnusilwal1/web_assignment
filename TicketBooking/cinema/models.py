from django.db import models

class Genre(models.Model):
    GENRE =[
        ('Action','ACTION'),
        ('Comedy','COMEDY'),
        ('Drama','DRAMA'),
        ('Horror','HORROR'),
        ('Romance','ROMANCE'),
        ('Thriller','THRILLER')
    ]
    name = models.CharField(max_length=200, choices=GENRE, default=None)
   
    def __str__(self):
        return self.name

class Director(models.Model):
    name=models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Cast(models.Model):
    name=models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name 


class Movie(models.Model):    
    name = models.CharField(max_length=200, default=None)
    runTime = models.IntegerField(default=None)
    genre = models.ManyToManyField(Genre, default=None)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, default=None)
    casts = models.ManyToManyField(Cast, default=None)
    trailer_url = models.CharField(max_length=200, default=None)
    poster_url = models.CharField(max_length=255, null=True, default=None)
   
    def __str__(self):
        return self.name