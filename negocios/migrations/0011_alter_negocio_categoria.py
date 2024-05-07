# Generated by Django 5.0.2 on 2024-05-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("negocios", "0010_alter_negocio_endereco"),
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
                    ("moveisPlanejados", "Moveis Planejados"),
                ],
                default="Indefinido",
                max_length=20,
            ),
        ),
    ]
