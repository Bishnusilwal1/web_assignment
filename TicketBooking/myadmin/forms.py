from django import forms
from Ticket.models import Show
from django.contrib.auth.models import User


class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show 
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = '__all__'

class AdminForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
>>>>>>> 720d29e76dacd579ae80cf71034433364c21f93c
