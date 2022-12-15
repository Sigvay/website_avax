from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from cars.models import *
from users.models import Users


def number_container():
    try:
        number = Container.objects.last()
        default = 0
        if number.id > default:
            default = number.id
        default += 1
    except AttributeError:
        default = 1
    return 'Sharjah-' + str(default)


def number_part():
    try:
        number = PurchasedEngines.objects.last()
        default = 0
        if number.id > default:
            default = number.id
        default += 1
    except AttributeError:
        default = 1
    return 'H' + str(default)


def last_container():
    con = Container.objects.last()
    return con


class Sellers(models.Model):
    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = '4. Продавцы'

    name = models.CharField(verbose_name='Название', max_length=250)
    geoposition = models.CharField(verbose_name='Геопозиция', max_length=250, blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=50)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Container(models.Model):
    class Meta:
        verbose_name = "Контейнер"
        verbose_name_plural = '3. Контейнеры'

    country = models.CharField(verbose_name='Страна получатель', max_length=250)
    name = models.CharField(verbose_name='Номер контейнера', max_length=255, unique=True, default=number_container)
    moving_warehouse = models.IntegerField(verbose_name='Стоимость перемещения к контейнеру $', blank=True, null=True,
                                           help_text='Общая стоимость всех перемещений моторов к контейнеру')
    loading_cost = models.IntegerField(verbose_name='Стоимость погрузки $', blank=True, null=True)
    transportation_costs = models.IntegerField(verbose_name='Стоимость перевозки $', blank=True, null=True)
    customs_clearance = models.IntegerField(verbose_name='Стоимость растарможки $', blank=True, null=True)
    move = models.BooleanField(verbose_name='В пути', help_text='Да если уехал, Нет еще загружается', default=False)
    arrived = models.BooleanField(verbose_name='Прибыл',
                                  help_text='Да - если прибыл в место назначения, нет - если еще в пути', default=False)

    def __str__(self):
        return f'Контейнер - {self.name}'


class PurchasedEngines(models.Model):
    class Meta:
        verbose_name = 'Купленный двигатель'
        verbose_name_plural = '1. Купленные двигателя'

    container = models.ForeignKey(Container, verbose_name='Контейнер',
                                  on_delete=models.PROTECT,
                                  default=last_container)  # установить по дефолту последний контейнер
    number = models.CharField(verbose_name='Разборочный', max_length=255, default=number_part)
    mark = models.ForeignKey(Mark, verbose_name='Марка авто', on_delete=models.PROTECT)
    model = models.ForeignKey(Model, verbose_name='Модель авто', on_delete=models.PROTECT)
    year = models.CharField(verbose_name='Год выпуска', max_length=10, blank=True, null=True)
    engine_mark = models.ForeignKey(Engines, verbose_name='Маркировка двигателя', on_delete=models.PROTECT)
    engine_number = models.CharField(verbose_name='Номер блока', max_length=255, blank=True, null=True)
    transmission = models.ForeignKey(Transmissions, verbose_name='Тип КПП', on_delete=models.PROTECT)
    description = models.ForeignKey(DescriptionEngnine, verbose_name='Описание', on_delete=models.PROTECT,
                                    blank=True, null=True)
    weigh = models.CharField(verbose_name='Вес мотора', max_length=100, blank=True, null=True)
    price = models.IntegerField(verbose_name='Стоимость запчасти', blank=True, null=True)
    warehouse = models.BooleanField(verbose_name='Перемещен на склад',
                                    help_text='Да - если на складе погрузки в контейнер, Нет - если на складе у продавца',
                                    default=False)
    order = models.BooleanField(verbose_name='Резерв', default=False)
    who_order = models.ForeignKey(Users, verbose_name='Заказчик', on_delete=models.PROTECT, blank=True, null=True)
    payment = models.CharField(verbose_name='Оплата/Предоплата', max_length=20, blank=True, null=True,
                               help_text='Указать стоимость оплаты или предоплаты', default='0')

    def __str__(self):
        return f'{self.mark} {self.model} ({self.engine_number})'


class EnginesInStock(models.Model):
    class Meta:
        verbose_name = 'Двигатель в наличии'
        verbose_name_plural = '2. Двигателя в наличии'

    mark = models.ForeignKey(Mark, verbose_name='Марка авто', on_delete=models.PROTECT)
    model = models.ForeignKey(Model, verbose_name='Модель авто', on_delete=models.PROTECT)
    year = models.CharField(verbose_name='Год выпуска', max_length=10, blank=True, null=True)
    engine_mark = models.ForeignKey(Engines, verbose_name='Маркировка двигателя', on_delete=models.PROTECT)
    transmission = models.ForeignKey(Transmissions, verbose_name='Тип КПП', on_delete=models.PROTECT)
    description = models.ForeignKey(DescriptionEngnine, verbose_name='Описание', on_delete=models.PROTECT,
                                    blank=True, null=True)
    price = models.IntegerField(verbose_name='Стоимость запчасти', blank=True, null=True)

    def __str__(self):
        return f'{self.mark} {self.model} {self.year} - {self.engine_mark} - {self.transmission} / {self.price}$'
