# Generated by Django 4.1.3 on 2023-03-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minsk', '0007_exportpriceavito_exchange_exportpriceavito_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportpriceavito',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='slug'),
        ),
    ]
