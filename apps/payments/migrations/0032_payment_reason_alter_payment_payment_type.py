# Generated by Django 4.0.5 on 2022-06-10 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0031_alter_payment_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='reason',
            field=models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.SmallIntegerField(choices=[(0, 'Compra'), (1, 'Pluses'), (2, 'Pago profesores/arcanos/uzzas'), (3, 'Pago estudiantes'), (4, 'Descuento estudiantes'), (5, 'Cambio de oros por Galeones'), (6, 'Recompensa por Mazmorras'), (99, 'Otros Depósitos'), (100, 'Otros Descuentos')], default=0, verbose_name='Tipo de pago'),
        ),
    ]