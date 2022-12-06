from django.db import models

from emirate.models import EnginesInStock
from users.models import Users


class OrderEmirate(models.Model):
    class Meta:
        verbose_name = 'Заказ Эмираты'
        verbose_name_plural = 'Заказы Эмираты'

    user = models.ForeignKey(Users, verbose_name='Заказчик', on_delete=models.CASCADE)
    engine = models.ForeignKey(EnginesInStock, verbose_name='Двигатель под заказ', on_delete=models.PROTECT)
    count = models.CharField(verbose_name='Количество', max_length=50, default='1')
    payment = models.CharField(verbose_name='Оплата/Предоплата', max_length=20, blank=True, null=True,
                               help_text='Указать стоимость оплаты или предоплаты', default='0')
    completed = models.BooleanField(verbose_name='Выполнен', default=False,
                                    help_text='Да - если закуплен, Нет - если на стадии выполнения')
