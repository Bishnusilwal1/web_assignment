from django.urls import path
from cinema import views

urlpatterns = [
    path("", views.index, name="index"),
    path('details/<int:mid>', views.movie_details, name="details"),
<<<<<<< HEAD
    path('searches/', views.search_view, name="searches"),
=======
<<<<<<< HEAD
    path('search/', views.search_movie, name="search"),
=======
    path('searches/', views.search_view, name="searches"),
>>>>>>> 3338aa60c56689aa9e0b2b4302d550cf2d0123d9
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
]
