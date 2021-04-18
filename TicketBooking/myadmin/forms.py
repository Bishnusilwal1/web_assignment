from django import forms
from Ticket.models import Show
from django.contrib.auth.models import User
from cinema.models import Movie, Genre, Cast, Director


class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show 
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = '__all__'


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie 
        fields = '__all__'
