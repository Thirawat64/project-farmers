# Generated by Django 4.2.2 on 2023-12-21 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_allproduct_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="allproduct",
            name="phon_number",
            field=models.CharField(default="location", max_length=10),
        ),
    ]