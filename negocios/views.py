from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Negocio


class ListaNegociosViews(ListView):
    model = Negocio
    template_name = 'listaDeNegocios.html'
    context_object_name = 'negocios'
    paginas = 9

    def get_queryset(self):
        return Negocio.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        negocios = self.get_queryset()
        paginator = Paginator(negocios, self.paginas)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['negocios'] = page_obj
        return context
