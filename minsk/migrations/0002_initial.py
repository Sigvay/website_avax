# Generated by Django 4.1.3 on 2022-12-06 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('minsk', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentminsk',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='photonouskat',
            name='nouskat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='minsk.nouskat', verbose_name='Ноускат'),
        ),
    ]