import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    job_title = models.CharField(max_length=150, verbose_name='Должность',choices=(('Chief', 'Начальник'),('Manager', 'Руководитель')))


    def __str__(self):
        return self.name


class Administrator(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    years_old = models.IntegerField(verbose_name='Лет', default=16,validators=[MinValueValidator(20), MaxValueValidator(100)])
    contact_number = models.IntegerField(verbose_name='Телефон', default=79001112233)
    data_passport = models.IntegerField(verbose_name='Паспорт', default=7777999888)

    def __str__(self):
        return self.name


class User_test(models.Model):
    name = models.CharField(max_length=100, verbose_name='Никнейм')
    visitor = models.CharField(max_length=20,verbose_name='Частый гость',choices=(('Yes', 'Да'),('No', 'Нет')))

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User_test, verbose_name='Имя клиента', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Статус заказа',max_length=50,choices=(('Open', 'Открыт'),('Close', 'Закрыт')))




    def __str__(self):
        return self.user.name