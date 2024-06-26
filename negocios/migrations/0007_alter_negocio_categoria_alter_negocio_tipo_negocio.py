# Generated by Django 5.0.2 on 2024-04-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("negocios", "0006_rename_negocios_negocio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="negocio",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("limpeza", "Limpeza"),
                    ("manutencao", "Manutenção"),
                    ("restaurante", "Restaurante"),
                    ("informatica", "Informática"),
                    ("beleza", "Beleza"),
                    ("moda", "Moda"),
                    ("alimentacao", "Alimentação"),
                    ("indefinido", "Indefinido"),
                    ("papelaria", "Papelaria"),
                ],
                default="Indefinido",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="negocio",
            name="tipo_negocio",
            field=models.CharField(
                choices=[("servico", "Prestador de Serviço"), ("comercio", "Comércio")],
                default="Prestador de serviço",
                max_length=21,
            ),
        ),
    ]
