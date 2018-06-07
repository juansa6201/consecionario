from django import forms
from django.http import request

from models import *
from django.contrib.auth.forms import UserCreationForm

class FormCompra(forms.ModelForm):
    class Meta:
        model = Purasche
        fields = ('brand', 'model', 'patent', 'price', 'repairs',)
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
                'placeholder': 'Ingrese la patente'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio'
            }),
            'repairs': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio de las reparaciones'
            }),
            #'user':forms.Select(attrs={'class':'form-control'})
        }


class FormVenta(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('sale', 'price', )

        widgets = {
            'sale': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio'
            }),

        }

    def __init__(self, user, *args, **kwargs):
        super(FormVenta, self).__init__(*args, **kwargs)
        self.fields['sale'].queryset = Purasche.objects.filter(user=user)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )