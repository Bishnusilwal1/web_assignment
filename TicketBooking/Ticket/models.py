from django.db import models
from django.contrib.auth.models import User



class Show(models.Model):
    STATUS =[
        ('Running','RUNNING'),('Finished','FINISHED'),('Started','STARTED')
    ]
    name = models.CharField(max_length=50, null=True, default=None)
    show_start_time=models.DateTimeField(default=None)
    end_start_time=models.DateTimeField(default=None)
    status=models.CharField(max_length=200, choices=STATUS, default=None)
    price = models.IntegerField(null=True, default=None)

    def __str__(self):
        return self.name 

class Cinema(models.Model):
    name=models.CharField(max_length=200, default=None)
    location=models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    book_date=models.DateTimeField(auto_now_add=True)
    show = models.ForeignKey(Show,null=True, on_delete=models.CASCADE, default=None)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, default=None)

    def __int__(self):
        return self.id 