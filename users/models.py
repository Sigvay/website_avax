from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = '1. Пользователи'

    mailing = models.BooleanField(verbose_name='Рассылка уведомлений', default=True,
                                  help_text='Будет ли получать пользователь сообщения с рекламой')
    shipping = models.BooleanField(verbose_name='Отправки ТК', default=False,
                                   help_text='Установите флажок если пользователю часто отправляют'
                                             'транспортными компаниями')
    exctended_profile = models.BooleanField(verbose_name='Расширенный профиль', default=False,
                                            help_text='Установите флажок если пользователю нужно предоставить'
                                                      ' доступ для постановки резерва')
    deny_access = models.BooleanField(verbose_name='Запретить доступ', default=False,
                                      help_text='Запрещает пользователю использовать приложение')
    id_telegram = models.CharField(verbose_name='id_telegram', max_length=50, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=15, blank=True)
    city = models.CharField(verbose_name='Город', max_length=255, blank=True)

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'


class UserRequest(models.Model):
    class Meta:
        verbose_name = 'Запрос пользователя'
        verbose_name_plural = '2. Запросы пользователей'

    user_id = models.ForeignKey(Users, verbose_name='пользователь', on_delete=models.PROTECT)
    query_name = models.CharField(verbose_name='Текс запроса', max_length=255, null=True, blank=True)
    date_query = models.DateTimeField(verbose_name='Дата запроса')
    available = models.CharField(verbose_name='В наличии', max_length=10)

    def __str__(self):
        return f'{self.date_query} - {self.user_id}-{self.query_name}'