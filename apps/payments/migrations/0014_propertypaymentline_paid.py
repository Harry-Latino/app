# Generated by Django 3.2.5 on 2021-07-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0013_propertypaymentline"),
    ]

    operations = [
        migrations.AddField(
            model_name="propertypaymentline",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]
