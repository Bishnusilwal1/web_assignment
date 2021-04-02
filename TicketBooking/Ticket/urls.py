
from django.urls import path

from Ticket import views

urlpatterns = [
<<<<<<< HEAD
    path('',views.index,name="ticket"),
=======
    path('',views.index,name="index"),
>>>>>>> 3338aa60c56689aa9e0b2b4302d550cf2d0123d9
    path('cinemas/',views.cinemas,name="cinemas"),
    path('tickets/',views.tickets,name="tickets"),
]