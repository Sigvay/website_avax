# Generated by Django 4.1.3 on 2022-12-11 17:38

from django.db import migrations, models
import django.db.models.deletion
import emirate.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=250, verbose_name='Страна получатель')),
                ('name', models.CharField(default=emirate.models.number_container, max_length=255, unique=True, verbose_name='Номер контейнера')),
                ('moving_warehouse', models.IntegerField(blank=True, help_text='Общая стоимость всех перемещений моторов к контейнеру', null=True, verbose_name='Стоимость перемещения к контейнеру $')),
                ('loading_cost', models.IntegerField(blank=True, null=True, verbose_name='Стоимость погрузки $')),
                ('transportation_costs', models.IntegerField(blank=True, null=True, verbose_name='Стоимость перевозки $')),
                ('customs_clearance', models.IntegerField(blank=True, null=True, verbose_name='Стоимость растарможки $')),
                ('move', models.BooleanField(default=False, help_text='Да если уехал, Нет еще загружается', verbose_name='В пути')),
                ('arrived', models.BooleanField(default=False, help_text='Да - если прибыл в место назначения, нет - если еще в пути', verbose_name='Прибыл')),
            ],
            options={
                'verbose_name': 'Контейнер',
                'verbose_name_plural': '3. Контейнеры',
            },
        ),
        migrations.CreateModel(
            name='EnginesInStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=10, null=True, verbose_name='Год выпуска')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Стоимость запчасти')),
            ],
            options={
                'verbose_name': 'Двигатель в наличии',
                'verbose_name_plural': '2. Двигателя в наличии',
            },
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('geoposition', models.CharField(blank=True, max_length=250, null=True, verbose_name='Геопозиция')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Продавец',
                'verbose_name_plural': '4. Продавцы',
            },
        ),
        migrations.CreateModel(
            name='PurchasedEngines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default=emirate.models.number_part, max_length=255, verbose_name='Разборочный')),
                ('year', models.CharField(blank=True, max_length=10, null=True, verbose_name='Год выпуска')),
                ('engine_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер блока')),
                ('weigh', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вес мотора')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Стоимость запчасти')),
                ('warehouse', models.BooleanField(default=False, help_text='Да - если на складе погрузки в контейнер, Нет - если на складе у продавца', verbose_name='Перемещен на склад')),
                ('order', models.BooleanField(default=False, verbose_name='Резерв')),
                ('payment', models.CharField(blank=True, default='0', help_text='Указать стоимость оплаты или предоплаты', max_length=20, null=True, verbose_name='Оплата/Предоплата')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emirate.container', verbose_name='Контейнер')),
                ('engine_mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.engines', verbose_name='Маркировка двигателя')),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.fuelengine', verbose_name='Топливо')),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.mark', verbose_name='Марка авто')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.model', verbose_name='Модель авто')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.transmissions', verbose_name='Тип КПП')),
            ],
            options={
                'verbose_name': 'Купленный двигатель',
                'verbose_name_plural': '1. Купленные двигателя',
            },
        ),
    ]
