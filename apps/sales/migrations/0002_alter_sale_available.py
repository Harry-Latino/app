# Generated by Django 3.2 on 2021-04-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="available",
            field=models.BooleanField(
                default=True,
                help_text="Este campo se utiliza para marcar una compra de libros de hechizos o consumiblesSpell books. True = Can UseConsumables. True = Consumable UsedCreatures. True = In the creature pool",
                verbose_name="Disponible?",
            ),
        ),
    ]
