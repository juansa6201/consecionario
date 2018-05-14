# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Purasche(models.Model):
    user = models.ForeignKey(User, blank=True)
    brand = models.CharField('Marca', max_length=20, null=False)
    model = models.CharField('Modelo', max_length=20, null=False)
    date_purasche = models.DateTimeField('Fecha de Compra', auto_now=True)
    patent = models.CharField('Patente', max_length=10, null=True)
    price = models.IntegerField('Precio', null=False)
    repairs = models.IntegerField('Reparaciones', null=False)

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

    class Meta():
        verbose_name = 'Compra'


class Sale(models.Model):
    user = models.ForeignKey(User)
    sale = models.ForeignKey(Purasche, related_name='aCount')
    price = models.IntegerField('Precio', null=False)
    sale.verbose_name = 'Venta'

    def __str__(self):
        return 'Vendio {} por {}'.format(self.sale, self.price)

    class Meta():
        verbose_name = 'Venta'
