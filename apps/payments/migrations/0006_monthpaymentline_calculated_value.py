# Generated by Django 3.2.3 on 2021-06-02 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0005_auto_20210602_1842"),
    ]

    operations = [
        migrations.AddField(
            model_name="monthpaymentline",
            name="calculated_value",
            field=models.IntegerField(default=0, verbose_name="Valor a pagar"),
        ),
    ]
