# Generated by Django 5.0.2 on 2024-04-12 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("negocios", "0005_alter_negocios_categoria"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Negocios",
            new_name="Negocio",
        ),
    ]