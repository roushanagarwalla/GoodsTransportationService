# Generated by Django 3.2.5 on 2022-02-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='quantity',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
