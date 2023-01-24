from django.db import models
from django.urls import reverse

from users.models import Users


class WarehouseMinsk(models.Model):
    class Meta:
        verbose_name = 'Наличие Минск'
        verbose_name_plural = '1. Наличие Минск'

    article = models.IntegerField(verbose_name='Артикул')
    mark_auto = models.CharField(verbose_name='Марка', max_length=100)
    model_auto = models.CharField(verbose_name='Модель', max_length=250)
    submodel_auto = models.CharField(verbose_name='Подмодель', max_length=250)
    year = models.IntegerField(verbose_name='Год')
    spare = models.CharField(verbose_name='Запчасть', max_length=100)
    fuel = models.CharField(verbose_name='Топливо', max_length=50)
    volume = models.FloatField(verbose_name='Объем', blank=True, null=True)
    type_engine = models.CharField(verbose_name='Тип двигателя', max_length=50)
    transmission = models.CharField(verbose_name='КПП', max_length=100)
    original_number = models.CharField(verbose_name='Маркировка', max_length=250, blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(verbose_name='Валюта', max_length=50)
    id_photo = models.CharField(verbose_name='id фото', max_length=10, blank=True)
    photo = models.TextField(verbose_name='Фото', blank=True, null=True)
    input_article = models.IntegerField(verbose_name='Разборочный')
    vin = models.CharField(verbose_name='VIN', max_length=20, blank=True, null=True)
    id_video = models.CharField(verbose_name='id видео', max_length=10, blank=True)
    video = models.CharField(verbose_name='Видео', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.article}/{self.input_article} - {self.mark_auto} {self.model_auto} - {self.original_number}'


class Nouskat(models.Model):
    class Meta:
        verbose_name = 'Ноускат'
        verbose_name_plural = '3. Ноускаты'

    mark = models.CharField(verbose_name='Марка', max_length=50)
    model = models.CharField(verbose_name='Модель', max_length=50)
    year = models.CharField(verbose_name='Год', max_length=10)
    color = models.CharField(verbose_name='Цвет', max_length=20)
    price = models.IntegerField(verbose_name='Цена')
    note = models.CharField(verbose_name='Примечание', max_length=255)
    active = models.BooleanField(verbose_name='Активный', default=True,
                                 help_text='Если установлен флажок, обьявление видно в боте')
    sold = models.BooleanField(verbose_name='Продано', default=False,
                               help_text='Если установлен флажок, обьявление продано')
    sale_price = models.IntegerField(verbose_name='Цена продажи', null=True, blank=True)

    def __str__(self):
        return f'{self.mark} {self.model}({self.year}) - {self.price}'


class PhotoNouskat(models.Model):
    nouskat_id = models.ForeignKey(Nouskat, verbose_name='Ноускат', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='public/image/')

    def __str__(self):
        return f'{self.image}'


class ShipmentMinsk(models.Model):
    class Meta:
        verbose_name = 'Отправка Минск'
        verbose_name_plural = '2. Отправки Минск'

    part = models.CharField(verbose_name='Запчасть', max_length=50)
    count = models.IntegerField(verbose_name='Колличество', null=True, blank=True)
    article = models.CharField(verbose_name='Разборочный', max_length=100, null=True, blank=True)
    tk = models.CharField(verbose_name='Транспортная', max_length=50)
    client = models.ForeignKey(Users, verbose_name='Клиент', null=True, blank=True, on_delete=models.PROTECT)
    city = models.CharField(verbose_name='Город', max_length=100, null=True, blank=True)
    type_send = models.CharField(verbose_name='Тип отправки', max_length=100)
    information = models.CharField(verbose_name='Информация', max_length=255, null=True, blank=True)
    username = models.CharField(verbose_name='Кто записал', max_length=20)
    track = models.CharField(verbose_name='Трек номер', max_length=50, null=True, blank=True)
    shipped = models.BooleanField(verbose_name='Отгружено', default=False,
                                  help_text='Если установлен флажок, значит уехало')
    date_add = models.DateTimeField(verbose_name='Дата')

    def __str__(self):
        return f'{self.client} - {self.tk} / {self.track}'


class ExportPrice(models.Model):
    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = '4. Прайсы'

    name = models.CharField(verbose_name='Название прайса', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    url = models.CharField(verbose_name='Ссылка', max_length=255, blank=True, null=True,
                           default='https://avaxdjango.herokuapp.com/minsk/export/')
    count = models.IntegerField(verbose_name='Колличество скачиваний', blank=True, null=True, default=0)
    date_last = models.DateTimeField(verbose_name='Дата последнего скачивания', blank=True, null=True)

    def show_url(self):
        return f'{self.url}{self.slug}'

    def __str__(self):
        return f'{self.name}'
