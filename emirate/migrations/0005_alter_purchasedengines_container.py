# Generated by Django 4.1.3 on 2022-12-15 22:37

from django.db import migrations, models
import django.db.models.deletion
import emirate.models


class Migration(migrations.Migration):

    dependencies = [
        ('emirate', '0004_enginesinstock_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedengines',
            name='container',
            field=models.ForeignKey(default=emirate.models.last_container, on_delete=django.db.models.deletion.PROTECT, to='emirate.container', verbose_name='Контейнер'),
        ),
    ]
