# Generated by Django 4.1.3 on 2023-01-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minsk', '0003_alter_shipmentminsk_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseminsk',
            name='input_article',
            field=models.IntegerField(verbose_name='Разборочный'),
        ),
    ]
