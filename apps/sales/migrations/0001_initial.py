# Generated by Django 3.1.7 on 2021-03-16 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
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
                ("date", models.DateField(verbose_name="Fecha")),
                (
                    "available",
                    models.BooleanField(
                        default=False,
                        help_text="Este campo se utiliza para marcar una compra de libros de hechizos o consumiblesSpell books. True = Can UseConsumables. True = Consumable UsedCreatures. True = In the creature pool",
                        verbose_name="Estado",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sales",
                        to="products.product",
                        verbose_name="Producto",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sales",
                        to="profiles.profile",
                        verbose_name="Comprador",
                    ),
                ),
            ],
            options={
                "verbose_name": "Venta",
                "verbose_name_plural": "Ventas",
                "ordering": ("date",),
                "abstract": False,
            },
        ),
    ]
