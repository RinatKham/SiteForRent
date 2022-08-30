from django.db import models


class CarModel(models.Model):
    title = models.CharField('Модель машины', max_length= 50, db_index=True)
    Power = models.IntegerField('Мощость')
    Volume = models.FloatField('Объем двигателя')
    Year = models.IntegerField('Год выпуска')
    DayPrice = models.IntegerField('Цена за сутки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

class RentModel(models.Model):
    name = models.CharField('Имя клиента', max_length= 50)
    mail = models.CharField('E-mail', max_length=50)
    CarName = models.ForeignKey('CarModel', on_delete = models.PROTECT)
    Data = models.DateField('Дата аренды')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

