# Generated by Django 4.1.3 on 2022-12-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionEngnine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Примечание к ДВС',
                'verbose_name_plural': '6. Примечания к ДВС',
            },
        ),
    ]