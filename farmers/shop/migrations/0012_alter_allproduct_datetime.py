# Generated by Django 4.2.2 on 2024-02-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0011_allproduct_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="allproduct",
            name="datetime",
            field=models.DateField(blank=True, null=True),
        ),
    ]
