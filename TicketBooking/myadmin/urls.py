from django.urls import path
from myadmin import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.home, name="dashboard"),
    path('', views.admin_login, name="adlogin"),
    path('adlogout/', views.admin_logout, name="adlogout"),
    path('theatre/', views.theatre, name="theatre"),
    path('add_theatre/', views.theatre_add, name="add_theatre"),
    path('update_theatre/<int:tid>/', views.update_theatre, name="update_theatre"),
    path('delete_theatre/<int:tid>/', views.theatre_delete, name="delete_theatre"),
    path('movies/', views.movie, name="movie"),

    path('add_movie/', views.movie_add, name="add_movie"),
    path('edit_movie/<int:id>/', views.edit_movie, name="edit_movie"),
    path('delete_movie/<int:id>/', views.movie_delete, name="delete_movie"),

    path('users/', views.users, name="users"),
    path('edit_user/<int:uid>/', views.user_edit, name="edit_user"),
    path('delete_user/<int:id>/', views.user_delete, name="delete_user"),

    path('cast/', views.cast, name="cast"),
    path('add_cast', views.cast_add, name="add_cast"),
    path('edit_cast/<int:tid>/', views.cast_edit, name="edit_cast"),
    path('delete_cast/<int:tid>/', views.cast_delete, name="delete_cast"),

    path('director/', views.director, name="director"),
    path('add_director', views.director_add, name="add_director"),
    path('edit_director/<int:did>/', views.director_edit, name="edit_director"),
    path('delete_director/<int:did>/', views.director_delete, name="delete_director"),


    path('genre/', views.genre, name="genre"),
    path('add_genre', views.genre_add, name="add_genre"),
    path('edit_genre/<int:gid>/', views.genre_edit, name="edit_genre"),
    path('delete_genre/<int:gid>/', views.genre_delete, name="delete_genre"),

    path('delete_ticket/<int:cid>/', views.ticket_delete, name="delete_ticket"),

    path('', views.admin_login, name="admin-login"),
    path('logout/', views.admin_logout, name="admin-logout"),
    path('ticket/', views.ticket_dash, name="ticket"),
    path('change_password/', auth_views.PasswordChangeView.as_view( template_name='admin1/adminchange_password.html', success_url = '/'), name='change_password'),path('', views.admin_login, name="admin-login"),

]
