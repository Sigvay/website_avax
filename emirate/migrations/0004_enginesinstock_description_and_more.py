# Generated by Django 4.1.3 on 2022-12-14 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_descriptionengnine'),
        ('emirate', '0003_remove_purchasedengines_fuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='enginesinstock',
            name='description',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.descriptionengnine', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='purchasedengines',
            name='description',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.descriptionengnine', verbose_name='Описание'),
        ),
    ]