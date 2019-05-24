from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from .models import Funcionario, Frequencia
from .forms import FrequenciaForm

from django.urls import reverse
from datetime import datetime
import socket

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.conf import settings
# Create your views here.
class homePage(ListView):
    model = Frequencia
    template_name = 'app_ponto/index.html'


def Sucesso(request):
    try:
        dados = Frequencia.objects.get(data=datetime.now().date())
    except:
        dados = {}
    return render(request, 'app_ponto/sucesso.html',{'dados':dados})


def Frequencia_View(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        user = request.user
        user = Funcionario.objects.get(usuario=user)
        IP = socket.gethostbyname(socket.gethostname())
        us = request.META['REMOTE_ADDR']
        try:
            ponto = Frequencia.objects.get(data=datetime.now().date(), funcionario=user)
            horario = ponto.funcionario.configuracao
            if ponto.entrada2 == None or ponto.saida2 == None:
                if ponto.tipo == False:
                    if ponto.entrada1 == None:
                        ponto.entrada1 = datetime.now()
                        if horario.entrada1.hour < ponto.entrada1.hour or ponto.entrada1.minute > horario.entrada1.minute+15:
                            ponto.status = False
                    else:
                        ponto.entrada2 = datetime.now()
                    ponto.tipo = True
                else:
                    if ponto.saida1 == None:
                        ponto.saida1 = datetime.now()
                    else:
                        ponto.saida2 = datetime.now()
                    ponto.tipo = False
                ponto.ip = IP
                ponto.save()
        except:
            Frequencia(entrada1=datetime.now(), status = True, tipo = True, ip = None, funcionario = user).save()
        
        return redirect('sucesso') # Redireciona depois do POST
    return render(request, 'app_ponto/ponto.html')

def do_login(request):
    if request.method =="POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/ponto')
    return render(request, 'app_ponto/login.html')

def do_logout(request):
    logout(request)
    return redirect('login')

def erro(request):
    return render(request, 'app_ponto/erro.html')