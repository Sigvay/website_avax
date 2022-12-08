from django.db import models


class Mark(models.Model):
    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = '1. Марки'

    name_mark = models.CharField(verbose_name='Название марки', max_length=255)

    def __str__(self):
        return f'{self.name_mark}'


class Model(models.Model):
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = '2. Модели'

    mark = models.ForeignKey(Mark, verbose_name='Марка авто', on_delete=models.PROTECT)
    model = models.CharField(verbose_name='Название модели', max_length=255)

    def __str__(self):
        return f'{self.model}'


class FuelEngine(models.Model):
    class Meta:
        verbose_name = 'Топливо'
        verbose_name_plural = '3. Топливо'

    name = models.CharField(verbose_name='Топливо', max_length=50)

    def __str__(self):
        return f'{self.name}'


class Transmissions(models.Model):
    class Meta:
        verbose_name = 'КПП'
        verbose_name_plural = '5. КПП'

    name = models.CharField(verbose_name='Тип кпп', max_length=100)

    def __str__(self):
        return f'{self.name}'


class Engines(models.Model):
    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = '4. Двигателя'

    mark = models.ForeignKey(Mark, verbose_name='Марка авто', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Маркировка двигателя', max_length=100)
    fuel = models.ForeignKey(FuelEngine, verbose_name='Топливо', on_delete=models.PROTECT)
    volume_engine = models.CharField(verbose_name='Обьем двигателя', max_length=50)
    type_engine = models.CharField(verbose_name='Тип двигателя', max_length=20)

    def __str__(self):
        return f'{self.name} ({self.volume_engine}{self.type_engine})'
