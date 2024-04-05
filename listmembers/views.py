from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import FormularioDeCadastro
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.


def modelo(request):
    return render(request, 'listmembers/model.html')


'''Função entrar funcionando (sem mensagens de erro)'''


def entrar(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('page-home'))
        else:
            form = FormularioDeCadastro()
            return render(request, 'listmembers/cadastreSe.html', {'form': form})

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('page-home'))
    else:
        return render(request, 'listmembers/login.html')


@login_required(login_url='page-login')
def home(request):
    return render(request, 'listmembers/home.html')


'''função cadastre-se funcionando (sem mensagem de erro)'''


def cadastre_se(request):
    if request.method == 'POST':
        form = FormularioDeCadastro(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            if User.objects.filter(username=usuario).exists():
                messages.error(
                    request, "Este nome de usuário já está em uso. Por favor, escolha outro.")
            elif User.objects.filter(email=email).exists():
                messages.error(
                    request, "Este endereço de email já está em uso. Por favor, escolha outro.")
            else:
                User.objects.create_user(
                    username=usuario, email=email, password=senha)
                messages.success(
                    request, "Conta criada com sucesso. Faça login para acessar.")
                return render(request, 'listmembers/login.html')
    else:
        form = FormularioDeCadastro()

    return render(request, 'listmembers/cadastreSe.html', {'form': form})


@login_required
def sair(request):
    logout(request)
    if not request.user.is_authenticated:
        return render(request, 'listmembers/logout.html')


def esqueciMinhaSenha(request):
    return render(request, 'listmembers/esqueciMinhaSenha.html')
