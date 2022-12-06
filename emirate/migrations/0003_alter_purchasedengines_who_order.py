# Generated by Django 4.1.3 on 2022-12-06 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emirate', '0002_purchasedengines_order_purchasedengines_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedengines',
            name='who_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
    ]
