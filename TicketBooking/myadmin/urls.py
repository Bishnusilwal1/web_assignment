from django.urls import path
from myadmin import views

urlpatterns = [
<<<<<<< HEAD
    path('dasboard/', views.home, name="dashboard"),
=======
<<<<<<< HEAD
    path('dashboard/', views.home, name="dashboard"),
    path('', views.admin_login, name="adlogin"),
    path('adlogout/', views.admin_logout, name="adlogout"),
=======
    path('dashboard/', views.home, name="admin-home"),
>>>>>>> 3338aa60c56689aa9e0b2b4302d550cf2d0123d9
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
    path('theatre/', views.theatre, name="theatre"),
    path('add_theatre/', views.theatre_add, name="add_theatre"),
    path('edit_theatre/<int:tid>/', views.theatre_edit, name="edit_theatre"),
    path('delete_theatre/<int:tid>/', views.theatre_delete, name="delete_theatre"),
    path('movies/', views.movie, name="movie"),
    path('add_movies/', views.movie_add, name="add_movie"),
    path('users/', views.users, name="users"),
<<<<<<< HEAD
    path('', views.admin_login, name="adlogin"),
    path('logout/', views.admin_logout, name="adlogout"),
=======
    path('', views.admin_login, name="admin-login"),
    path('logout/', views.admin_logout, name="admin-logout"),
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
]
