# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.

class PurascheAdmin(admin.ModelAdmin):
    def SalesCount(self, obj):
        if obj:
            return obj.aCount.count()
    SalesCount.short_description = 'Contador de ventas'

    list_display = ('brand', 'model', 'price', 'repairs')
    list_filter = ('brand', 'model', 'patent')
    search_fields = ('brand', 'model')
    readonly_fields = ('SalesCount',)

class SaleAdmin (admin.ModelAdmin):
    list_display = ('sale', 'price')
    list_filter = ('sale', 'price')
    search_fields = ('price',)


admin.site.register(Purasche, PurascheAdmin)
admin.site.register(Sale, SaleAdmin)
