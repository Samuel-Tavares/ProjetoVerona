# Generated by Django 5.0.2 on 2024-04-09 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("negocios", "0003_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="negocios",
            old_name="telefone",
            new_name="contato_telefonico",
        ),
        migrations.AddField(
            model_name="negocios",
            name="tipo_de_contato",
            field=models.CharField(
                choices=[
                    ("wpp e atende", "WhatsApp/Atende ligações"),
                    ("wpp e nao atende", "WhatsApp/Não atende ligações"),
                    ("chamada", "Somente ligações"),
                ],
                default="Somente ligações",
                max_length=50,
            ),
        ),
    ]
