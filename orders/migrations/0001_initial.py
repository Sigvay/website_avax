# Generated by Django 4.1.3 on 2022-12-06 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emirate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderEmirate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(default='1', max_length=50, verbose_name='Количество')),
                ('payment', models.CharField(blank=True, default='0', help_text='Указать стоимость оплаты или предоплаты', max_length=20, null=True, verbose_name='Оплата/Предоплата')),
                ('completed', models.BooleanField(default=False, help_text='Да - если закуплен, Нет - если на стадии выполнения', verbose_name='Выполнен')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emirate.enginesinstock', verbose_name='Двигатель под заказ')),
            ],
            options={
                'verbose_name': 'Заказ Эмираты',
                'verbose_name_plural': 'Заказы Эмираты',
            },
        ),
    ]