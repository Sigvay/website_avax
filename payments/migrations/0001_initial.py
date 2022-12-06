# Generated by Django 4.1.3 on 2022-12-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField(verbose_name='Сумма')),
                ('article', models.CharField(max_length=255, verbose_name='Разборочный')),
                ('information', models.CharField(max_length=255, verbose_name='Информация')),
                ('username', models.CharField(max_length=20, verbose_name='Кто записал')),
                ('date_add', models.DateTimeField(verbose_name='Дата')),
                ('warehouse', models.CharField(blank=True, max_length=50, null=True, verbose_name='склад')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
    ]
