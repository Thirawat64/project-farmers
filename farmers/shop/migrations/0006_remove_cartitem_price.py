# Generated by Django 4.2.2 on 2024-02-26 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_cart_cartitem_delete_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="price",
        ),
    ]
