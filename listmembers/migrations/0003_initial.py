# Generated by Django 5.0.2 on 2024-04-09 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("listmembers", "0002_delete_morador_delete_prestadordeservico"),
    ]

    operations = [
        migrations.CreateModel(
            name="Negocios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo_negocio",
                    models.CharField(
                        choices=[
                            ("servico", "Prestador de Serviço"),
                            ("comercio", "Comércio"),
                        ],
                        default="Indefinido",
                        max_length=21,
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("endereco", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("descricao", models.TextField()),
                ("endereco_site", models.URLField(blank=True, null=True)),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("limpeza", "Limpeza"),
                            ("manutencao", "Manutenção"),
                            ("restaurante", "Restaurante"),
                            ("informatica", "Informática"),
                            ("beleza", "Beleza"),
                            ("moda", "Moda"),
                            ("alimentacao", "Alimentação"),
                            ("indefinido", "Indefinido"),
                        ],
                        default="Prestador de Serviço",
                        max_length=20,
                    ),
                ),
                ("avaliacao", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
