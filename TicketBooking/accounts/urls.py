from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.user_login, name="login"),
    path('register', views.user_register, name="register"),
    path('logout', views.user_logout, name="logout"),
    path('profile', views.user_account, name="profile"),
    path('change_password/', auth_views.PasswordChangeView.as_view( template_name='ticket/change_password.html', success_url = '/'), name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="ticket/passwordReset.html"), name="password_reset"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="ticket/passwordChangeDone.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="ticket/passworda_rest_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]


