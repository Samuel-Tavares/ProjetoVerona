# Generated by Django 5.0.2 on 2024-10-21 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("negocios", "0009_alter_negocio_categoria"),
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
                    ("moveis planejados", "Moveis Planejados"),
                    ("imobiliaria", "Imobiliária"),
                    ("marcenaria", "Marcenaria"),
                    ("eventos", "Eventos"),
                    ("decoracao", "Decoração"),
                    ("grafica", "Grafica"),
                    ("farmacia", "Farmácia"),
                    ("montagem", "Montagem"),
                    ("para seu pet", "Para seu PET"),
                    ("entretenimento", "Entretenimento"),
                    ("seguros", "Seguros"),
                    ("marmores", "Marmores"),
                    ("advocacia", "Advocacia"),
                ],
                default="Indefinido",
                max_length=20,
            ),
        ),
    ]
