from django.urls import path
from negocios.views import ListaNegociosViews
from negocios import views


urlpatterns = [
    path('contatos/', ListaNegociosViews.as_view(), name='lista_negocios'),
    path('sobre/', views.sobre_view, name='sobre'),
]
