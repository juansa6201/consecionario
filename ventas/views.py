# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone

from .forms import *
from models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def home(request):
    return render(request,'home.html')

def index(request):
    todo = {
        'compras': Purasche.objects.filter(user=request.user),
        'ventas': Sale.objects.filter(user=request.user)
    }
    return render(request, 'tabla.html', todo)


def post_compra(request):
    if request.method == "POST":
        form = FormCompra(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = FormCompra()

    return render(request, 'compras.html', {'form': form})


def post_ventas(request):
    if request.method == "POST":
        form = FormVenta(request.user, request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = FormVenta(request.user)


    return render(request, 'ventas.html', {'form': form})

# Create your views here.
