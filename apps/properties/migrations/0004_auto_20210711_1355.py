# Generated by Django 3.2.5 on 2021-07-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0003_auto_20210711_1322"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="property",
            options={"verbose_name": "propiedad", "verbose_name_plural": "propiedades"},
        ),
        migrations.AlterField(
            model_name="property",
            name="name",
            field=models.CharField(max_length=128, unique=True, verbose_name="Nombre"),
        ),
    ]
