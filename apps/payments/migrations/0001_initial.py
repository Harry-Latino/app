# Generated by Django 3.2.3 on 2021-05-31 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Work",
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
                ("work", models.CharField(max_length=256, verbose_name="Trabajo")),
                (
                    "work_description",
                    models.TextField(verbose_name="Descripción del trabajo"),
                ),
                (
                    "wizard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profiles.profile",
                        verbose_name="Usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Trabajo",
                "verbose_name_plural": "Trabajos",
                "ordering": ("wizard__forum_user_id",),
                "abstract": False,
            },
        ),
    ]
