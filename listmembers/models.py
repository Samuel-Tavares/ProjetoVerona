from django.db import models


class Morador(models.Model):
    primeiroNome = models.CharField("nome", max_length=50)
    ultimoNome = models.CharField("sobrenome", max_length=50)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.usuario


class Prestador(models.Model):
    nomeRazaoSocial = models.CharField("nome/Razão Social", max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
