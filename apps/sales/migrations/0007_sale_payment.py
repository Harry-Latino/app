# Generated by Django 4.0.3 on 2022-03-21 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0029_alter_payment_options_alter_paymentline_options'),
        ('sales', '0006_alter_sale_options_sale_consumable_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='payment',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.payment', verbose_name='Pago'),
        ),
    ]