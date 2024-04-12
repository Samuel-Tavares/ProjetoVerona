from django.urls import path
from .views import ListaNegociosViews

urlpatterns = [
    path('contatos/', ListaNegociosViews.as_view(), name='lista_negocios'),
]
