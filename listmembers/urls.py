from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='page-login'),
    path('listmembers/home', views.home, name='page-home'),
    path('listmembers/cadastreSe', views.cadastreSe, name='page-cadastreSe'),
    path('listmembers/esqueciMinhaSenha',
         views.esqueciMinhaSenha, name='page-esqueciMinhaSenha'),
    path('listmembers/model', views.model, name='page-model'),
]
