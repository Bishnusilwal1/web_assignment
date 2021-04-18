from django.urls import path, re_path
from cinema import views

urlpatterns = [
    path("", views.index, name="index"),
    path('details/<int:mid>', views.movie_details, name="details"),
    path('searches/', views.search_view, name="searches"),

]
