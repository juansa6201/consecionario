from django import forms
from django.http import request

from models import *


class FormCompra(forms.ModelForm):
    class Meta:
        model = Purasche
        fields = ('brand', 'model', 'patent', 'price' ,'repairs', 'user')

class FormVenta(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('sale','price','user',)

    def __init__(self, user, *args, **kwargs):
        super(FormVenta, self).__init__(*args, **kwargs)
        self.fields['sale'].queryset = Purasche.objects.filter(user=user)


