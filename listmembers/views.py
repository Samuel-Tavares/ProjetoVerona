from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return render(request, 'listmembers/login.html')


def model(request):
    return render(request, 'listmembers/model.html')

def home(request):
    return render(request, 'listmembers/home.html')

def cadastreSe(request):
    return render(request, 'listmembers/cadastreSe.html')

def esqueciMinhaSenha(request):
    return render(request, 'listmembers/esqueciMinhaSenha.html')
