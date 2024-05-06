from django.db import models


class Negocio(models.Model):
    TIPO_DE_NEGOCIO_CHOICES = (
        ('servico', 'Prestador de Serviço'),
        ('comercio', 'Comércio'),
    )

    CATEGORIA_CHOICES = (
        ('limpeza', 'Limpeza'),
        ('manutencao', 'Manutenção'),
        ('restaurante', 'Restaurante'),
        ('informatica', 'Informática'),
        ('beleza', 'Beleza'),
        ('moda', 'Moda'),
        ('alimentacao', 'Alimentação'),
        ('indefinido', 'Indefinido'),
        ('papelaria', 'Papelaria'),
    )

    TIPO_DE_CONTATO = (
        ('wpp e atende', 'WhatsApp/Atende ligações'),
        ('wpp e nao atende', 'WhatsApp/Não atende ligações'),
        ('chamada', 'Somente ligações'),
    )

    tipo_negocio = models.CharField(
        max_length=21, choices=TIPO_DE_NEGOCIO_CHOICES, default='Prestador de serviço')
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    contato_telefonico = models.CharField(max_length=15)
    tipo_de_contato = models.CharField(
        max_length=50, choices=TIPO_DE_CONTATO, default='Somente ligações')
    email = models.EmailField(blank=True, null=True)
    descricao = models.TextField()
    endereco_site = models.URLField(blank=True, null=True)
    whatsappContato = models.CharField(blank=True, null=True)
    categoria = models.CharField(
        max_length=20, choices=CATEGORIA_CHOICES, default='Indefinido')
    avaliacao = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nome
