# Generated by Django 3.1.4 on 2022-01-11 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
