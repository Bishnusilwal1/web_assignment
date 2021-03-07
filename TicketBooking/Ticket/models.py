from django.db import models

# Create your models here.
class Movie(models.Model):    
    name = models.CharField(max_length=200)
    runTime = models.IntegerField()
    trailer_url = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name

class Cinema(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField( max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    GENRE =[
        ('Action','ACTION'),
        ('Comedy','COMEDY'),
        ('Drama','DRAMA'),
        ('Horror','HORROR'),
        ('Romance','ROMANCE'),
        ('Thriller','THRILLER')
    ]
    name = models.CharField(max_length=200, choices=GENRE)
    movie = models.ManyToManyField(Movie)
   
    def __str__(self):
        return self.name

class Director(models.Model):
    name=models.CharField( max_length=100)
    director_name = models.ManyToManyField(Movie)

    def __str__(self):
        return self.director_name


class Cast(models.Model):
    name=models.CharField( max_length=100)
    cast_name = models.ManyToManyField(Movie)

    def __str__(self):
        return self.cast_name    


    

class User(models.Model):
    GENDER =[
        ('M','MALE'),('F','Female'),('O','Other')
    ]
    email=models.CharField( max_length=100)
    username=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    Phone=models.IntegerField()
    dob=models.IntegerField()
    location=models.CharField(max_length=50)
    Gender=models.CharField( max_length=50, choices=GENDER)

    def __str__(self):
        return self.username 



class Ticket(models.Model):
    book_date=models.IntegerField()
    movie_date=models.IntegerField()

 


class Show(models.Model):
    STATUS =[
        ('R','RUNNING'),('F','FINISHED'),('S','STARTED')
    ]
    location=models.CharField(max_length=50)
    show_start_time=models.IntegerField()
    status=models.CharField( max_length=200)

    def __str__(self):
        return self.location 


