# Generated by Django 3.2.5 on 2021-08-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_alter_category_available_by_default"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="initial_stock",
            field=models.PositiveIntegerField(default=1, verbose_name="Stock inicial"),
        ),
    ]
