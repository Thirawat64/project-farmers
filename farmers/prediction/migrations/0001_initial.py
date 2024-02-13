# Generated by Django 4.2.2 on 2024-02-13 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph_value', models.FloatField()),
                ('max_temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('precip', models.FloatField(max_length=100)),
                ('soil_type', models.CharField(max_length=100)),
                ('area_slope', models.FloatField(max_length=100)),
                ('drainage', models.CharField(max_length=100)),
                ('predicted_plant', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]