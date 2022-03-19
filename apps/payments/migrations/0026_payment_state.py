# Generated by Django 3.2.9 on 2021-11-15 00:10

import apps.payments.workflows
from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0025_auto_20211114_1820"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="state",
            field=django_fsm.FSMIntegerField(
                choices=[(0, "Cancelado"), (1, "Creado"), (2, "Pagado")],
                default=apps.payments.workflows.PaymentWorkflow.Choices["CREATED"],
                protected=True,
                verbose_name="estado",
            ),
        ),
    ]