# Generated by Django 4.1.3 on 2023-04-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minsk', '0009_alter_exportpriceavito_adress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportpriceavito',
            name='exchange',
            field=models.IntegerField(verbose_name='Курс валюты'),
        ),
    ]