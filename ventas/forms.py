from django import forms
from django.http import request

from models import *


class FormCompra(forms.ModelForm):
    class Meta:
        model = Purasche
        fields = ('brand', 'model', 'patent', 'price', 'repairs', 'user')
        widgets = {
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la marca'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el modelo'
            }),
            'patent': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio'
            }),
            'repairs': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio'
            }),
            'user':forms.Select(attrs={'class':'form-control'})
        }


class FormVenta(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('sale', 'price', 'user',)

        widgets = {
            'sale': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese las reparaciones'
            }),
            'user':forms.Select(attrs={'class':'form-control'})
        }

    def __init__(self, user, *args, **kwargs):
        super(FormVenta, self).__init__(*args, **kwargs)
        self.fields['sale'].queryset = Purasche.objects.filter(user=user)
