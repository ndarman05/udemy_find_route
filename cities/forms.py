from django import forms

from cities.models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Введите название города',
    }), label='Город')

    class Meta:
        model = City
        fields = ('name', )
