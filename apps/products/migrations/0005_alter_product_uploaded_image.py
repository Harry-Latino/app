# Generated by Django 3.2.2 on 2021-05-09 02:44

import apps.products.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_product_uploaded_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="uploaded_image",
            field=models.ImageField(
                null=True,
                upload_to=apps.products.utils.get_upload_path,
                verbose_name="Imagen",
            ),
        ),
    ]
