# Generated by Django 3.2.3 on 2021-06-02 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0004_auto_20210601_1527"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="monthpaymentline",
            unique_together={("work", "month")},
        ),
        migrations.RemoveField(
            model_name="monthpaymentline",
            name="value",
        ),
    ]
