from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrar, name='page-login'),
    path('home/', views.home, name='page-home'),
    path('cadastreSe/', views.cadastre_se, name='page-cadastreSe'),
    path('esqueciMinhaSenha/',
         views.esqueciMinhaSenha, name='page-esqueciMinhaSenha'),
    path('model/', views.modelo, name='page-modelo'),
    path('logout/', views.sair, name='page-logout'),
]
