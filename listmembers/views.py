from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def model(request):
    return render(request, 'listmembers/model.html')


def entrar(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('home/')

    return render(request, 'listmembers/login.html')


@login_required(login_url='page-login')
def home(request):
    return HttpResponse('home')


def cadastre_se(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        email = request.POST['email']
        senha = request.POST['senha']

        if User.objects.filter(username=usuario).exists():
            return HttpResponse('Usuário já cadastrado')
            '''return render(request, 'listmembers/cadastreSe.html')'''
        else:
            novoUsuario = User.objects.create_user(
                username=usuario, email=email, password=senha)
            novoUsuario.save()

            return render(request, 'listmembers/login.html')

    else:
        return render(request, 'listmembers/cadastreSe.html')


def esqueciMinhaSenha(request):
    return render(request, 'listmembers/esqueciMinhaSenha.html')
