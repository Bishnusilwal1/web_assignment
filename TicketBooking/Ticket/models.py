from django.db import models
from django.contrib.auth.models import User
from cinema.models import Movie

class Cinema(models.Model):
    name=models.CharField(max_length=200, default=None)
    location=models.CharField(max_length=50, default=None)
    movie = models.ManyToManyField(Movie)
    def __str__(self):
        return self.name


class Show(models.Model):
    STATUS =[
        ('Running','RUNNING'),('Finished','FINISHED'),('Started','STARTED')
    ]
    name = models.CharField(max_length=50, null=True, default=None)
    show_start_time=models.DateTimeField(default=None)
    show_end_time=models.DateTimeField(default=None)
    status=models.CharField(max_length=200, choices=STATUS, default=None)
    price = models.IntegerField(null=True, default=None)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

class Ticket(models.Model):
    ticket_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    book_date=models.DateTimeField(auto_now_add=True)
    show = models.ForeignKey(Show,null=True, on_delete=models.CASCADE, default=None)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, default=None)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField()

    def __int__(self):
        return self.id 