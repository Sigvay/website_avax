# Generated by Django 4.1.3 on 2023-04-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minsk', '0008_alter_exportpriceavito_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportpriceavito',
            name='adress',
            field=models.CharField(blank=True, help_text='Обязательно так - "Россия, Москва, поселение Московский, МКАД, 47-й километр, 35соор6"', max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='exportpriceavito',
            name='contact',
            field=models.CharField(blank=True, help_text='Пример - "+79165147176"', max_length=255, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='exportpriceavito',
            name='manager_name',
            field=models.CharField(blank=True, help_text='Пример - "Александр"', max_length=255, null=True, verbose_name='Имя менеджера'),
        ),
    ]
