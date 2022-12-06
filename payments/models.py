from django.db import models


class Payment(models.Model):
    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    sum = models.IntegerField(verbose_name='Сумма')
    article = models.CharField(verbose_name='Разборочный', max_length=255)
    information = models.CharField(verbose_name='Информация', max_length=255)
    username = models.CharField(verbose_name='Кто записал', max_length=20)
    date_add = models.DateTimeField(verbose_name='Дата')
    warehouse = models.CharField(verbose_name='склад', max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.sum} - {self.article} / {self.username}'
