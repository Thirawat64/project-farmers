# Generated by Django 4.2.2 on 2024-03-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_sell_buy"),
    ]

    operations = [
        migrations.AddField(
            model_name="allproduct",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]