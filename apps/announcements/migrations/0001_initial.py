# Generated by Django 3.2 on 2021-04-08 18:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="fecha de creación"
                    ),
                ),
                (
                    "created_user",
                    models.CharField(
                        editable=False,
                        max_length=128,
                        null=True,
                        verbose_name="creado por",
                    ),
                ),
                (
                    "modified_date",
                    models.DateTimeField(
                        auto_now=True, verbose_name="última fecha de modificación"
                    ),
                ),
                (
                    "modified_user",
                    models.CharField(
                        editable=False,
                        max_length=128,
                        null=True,
                        verbose_name="modificado por",
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="activo")),
                (
                    "name",
                    models.CharField(max_length=256, verbose_name="Nombre del anuncio"),
                ),
                ("content", ckeditor.fields.RichTextField()),
            ],
            options={
                "verbose_name": "Anuncio",
                "verbose_name_plural": "Anuncios",
                "abstract": False,
            },
        ),
    ]
