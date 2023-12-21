from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404
import json
from django.http import JsonResponse

@login_required(login_url='/login/')
def home(request):
     return render(request, 'index.html')

def login_user(request):
    return render(request, 'login.html')

def index(request):
    return redirect('/home/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')