# Generated by Django 3.2.5 on 2021-08-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0015_propertypaymentline_paid_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="monthpayment",
            name="payment_post",
            field=models.URLField(
                blank=True, null=True, verbose_name="Link del pedido de pago"
            ),
        ),
    ]
