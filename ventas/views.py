# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
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

    return render(request, 'compras.html',{'form': form})


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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
# Create your views here.
