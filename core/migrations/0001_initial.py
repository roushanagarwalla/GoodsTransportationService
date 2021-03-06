# Generated by Django 3.2.5 on 2022-02-11 15:09

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
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mob', models.CharField(max_length=20)),
                ('truck_no', models.CharField(max_length=20)),
                ('truck_capacity', models.IntegerField()),
                ('transporter_name', models.CharField(max_length=100)),
                ('driving_experience', models.IntegerField()),
                ('from_state1', models.CharField(max_length=100)),
                ('from_city1', models.CharField(max_length=100)),
                ('to_state1', models.CharField(max_length=100)),
                ('to_city1', models.CharField(max_length=100)),
                ('from_state2', models.CharField(max_length=100)),
                ('from_city2', models.CharField(max_length=100)),
                ('to_state2', models.CharField(max_length=100)),
                ('to_city2', models.CharField(max_length=100)),
                ('from_state3', models.CharField(max_length=100)),
                ('from_city3', models.CharField(max_length=100)),
                ('to_state3', models.CharField(max_length=100)),
                ('to_city3', models.CharField(max_length=100)),
                ('rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mob', models.CharField(max_length=20)),
                ('nature', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('from_state', models.CharField(max_length=100)),
                ('from_city', models.CharField(max_length=100)),
                ('to_state', models.CharField(max_length=100)),
                ('to_city', models.CharField(max_length=100)),
                ('rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
