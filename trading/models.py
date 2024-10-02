from django.contrib.auth.models import User
from django.db import models

from config import NULLABLE

# Create your models here.


class Supplier(models.Model):

    title = models.CharField(max_length=255, verbose_name='название')
    email = models.CharField(max_length=255, verbose_name='электронная почта')
    country = models.CharField(max_length=128, verbose_name='страна')
    city = models.CharField(max_length=128, verbose_name='город')
    street = models.CharField(max_length=128, verbose_name='улица')
    house = models.CharField(max_length=32, verbose_name='дом')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')

    supplier = models.ForeignKey("self", **NULLABLE, on_delete=models.SET_NULL, verbose_name='поставщик')
    debt = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='задолженность')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):

    title = models.CharField(max_length=255, verbose_name='название')
    model = models.CharField(max_length=128, verbose_name='модель')
    launch_date = models.DateField(**NULLABLE, verbose_name='дата начала продаж')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f'{self.title} ({self.model})'
