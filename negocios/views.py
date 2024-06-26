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
        queryset = Negocio.objects.all()
        categoria = self.request.GET.get('categoria')
        tipo_negocio = self.request.GET.get('tipo_negocio')

        if categoria:
            queryset = queryset.filter(categoria=categoria)
        if tipo_negocio:
            queryset = queryset.filter(tipo_negocio=tipo_negocio)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        negocios = self.get_queryset()
        paginator = Paginator(negocios, self.paginas)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context['categorias'] = Negocio.CATEGORIA_CHOICES
        context['tipos_negocio'] = Negocio.TIPO_DE_NEGOCIO_CHOICES
        context['negocios'] = page_obj

        return context


def sobre_view(request):
    sobre_plataforma = 'A plataforma "Verona | Indica" é um projeto universitário e sem fins lucrativos que surgiu com a motivação de promover uma melhor qualidade de vida aos usuários, tornando fácil a procura por serviços indicados pelos condôminos. Ela ajuda os grandes, médios e pequenos empreendedores, além de promover a inclusão digital da comunidade.'

    return render(request, 'sobre.html', {'sobre_plataforma': sobre_plataforma})
