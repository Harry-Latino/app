# Generated by Django 3.2.3 on 2021-06-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0002_auto_20210601_1520"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="salary_scale",
            field=models.TextField(
                default="T0",
                editable=False,
                max_length=2,
                verbose_name="escalafón laboral",
            ),
        ),
    ]
