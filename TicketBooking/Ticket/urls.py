
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login_page,name="login"),
    path('register/',views.reg_page,name="register"),
    
]