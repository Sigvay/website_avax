# Generated by Django 4.1.3 on 2023-02-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='exctended_profile',
            field=models.BooleanField(default=False, help_text='Установите флажок если пользователю нужно предоставить доступ для постановки резерва', verbose_name='Расширенный профиль'),
        ),
    ]
