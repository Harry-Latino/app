# Generated by Django 3.2.5 on 2021-07-11 15:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profiles", "0006_alter_profile_accumulated_posts"),
    ]

    operations = [
        migrations.CreateModel(
            name="Family",
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
                    models.CharField(
                        max_length=128, unique=True, verbose_name="Nombre de la familia"
                    ),
                ),
                ("content", ckeditor.fields.RichTextField(verbose_name="Contenido")),
                (
                    "vault",
                    models.IntegerField(unique=True, verbose_name="Número de bóveda"),
                ),
                (
                    "owner",
                    models.ManyToManyField(
                        to="profiles.Profile", verbose_name="Propietarios/Patriarcas"
                    ),
                ),
            ],
            options={
                "verbose_name": "Familia",
                "verbose_name_plural": "Familias",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Business",
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
                    models.CharField(
                        max_length=128, unique=True, verbose_name="Nombre de la familia"
                    ),
                ),
                ("content", ckeditor.fields.RichTextField(verbose_name="Contenido")),
                (
                    "vault",
                    models.IntegerField(unique=True, verbose_name="Número de bóveda"),
                ),
                (
                    "owner",
                    models.ManyToManyField(
                        to="profiles.Profile", verbose_name="Propietarios/Patriarcas"
                    ),
                ),
            ],
            options={
                "verbose_name": "Negocio",
                "verbose_name_plural": "Negocios",
                "ordering": ("id",),
            },
        ),
    ]