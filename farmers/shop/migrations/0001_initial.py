# Generated by Django 4.2.2 on 2023-12-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllProduct",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=200)),
                ("product_price", models.IntegerField()),
                ("product_detail", models.TextField(default="No description")),
                (
                    "product_size",
                    models.CharField(default="Default Size", max_length=200),
                ),
                (
                    "product_status",
                    models.CharField(default="Default status", max_length=200),
                ),
                (
                    "product_location",
                    models.CharField(default="location", max_length=200),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
            ],
        ),
    ]
