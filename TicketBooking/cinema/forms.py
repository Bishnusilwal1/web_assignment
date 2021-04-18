from django import forms
from cinema.models import Cast, Genre, Director

class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
