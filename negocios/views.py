from django.shortcuts import render
from django.views.generic import ListView
from .models import Negocio


class ListaNegociosViews(ListView):
    model = Negocio
    template_name = 'listaDeNegocios.html'
    context_object_name = 'negocios'
