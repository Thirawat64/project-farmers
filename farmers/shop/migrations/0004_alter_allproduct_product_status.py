# Generated by Django 4.2.2 on 2023-12-20 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_status_alter_allproduct_product_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="allproduct",
            name="product_status",
            field=models.ForeignKey(
                blank=True,
                default="status",
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.status",
            ),
        ),
    ]
