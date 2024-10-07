from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


from config import NULLABLE

# Create your models here.


class Supplier(models.Model):
    """Implementation of the Supplier model."""

    LEVELS_CHOICES = {
        "factory": "factory",
        "retail": "retail network",
        "trader": "individual entrepreneur",
    }

    title = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(verbose_name='электронная почта')
    country = models.CharField(max_length=128, verbose_name='страна')
    city = models.CharField(max_length=128, verbose_name='город')
    street = models.CharField(max_length=128, verbose_name='улица')
    house = models.CharField(max_length=32, verbose_name='дом')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')

    level = models.CharField(max_length=10, default=LEVELS_CHOICES["factory"],
                             choices=LEVELS_CHOICES, verbose_name='уровень')
    vendor = models.ForeignKey("self", **NULLABLE, on_delete=models.SET_NULL, verbose_name='продавец')
    debt = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='задолженность')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    # products = models.ManyToManyField("product", related_name="products")

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'

    def __str__(self):
        return f'{self.title}'

    def clean(self):
        """Implementation of the logic of the seller-supplier relationship.
        in the order of factory-retail-trader
        """
        if self.vendor and self.id == self.vendor.id:
            raise ValidationError('Нельзя установить поставщиком тот же самый объект.')
        if self.level == 'factory' and (self.vendor and self.vendor.level != 'factory'):
            raise ValidationError('Завод может иметь поставщиком только другой завод.')
        if self.level == 'retail' and (not self.vendor or self.vendor.level not in ['factory', 'retail']):
            raise ValidationError('Розничная сеть должна иметь поставщиком завод или другую розничную сеть.')
        if self.level == 'trader' and (not self.vendor or self.vendor.level not in ['factory', 'retail', 'trader']):
            raise ValidationError('ИП должен иметь поставщиком завод, розничную сеть или другого ИП.')


class Product(models.Model):
    """Implementation of the Product model."""

    title = models.CharField(max_length=255, verbose_name='название')
    model = models.CharField(max_length=128, verbose_name='модель')
    launch_date = models.DateField(**NULLABLE, verbose_name='дата начала продаж')

    supplier = models.ForeignKey("supplier", on_delete=models.CASCADE, verbose_name='производитель')
    in_production = models.BooleanField(default=True, verbose_name='производится')

    class Meta:
        verbose_name = 'продукция'
        verbose_name_plural = 'продукция'

    def __str__(self):
        return f'{self.title} ({self.model})'

    def clean(self):
        """Only a factory can produce a product."""
        if self.supplier.level != 'factory':
            raise ValidationError('Производить продукцию может только завод.')


class Stock(models.Model):
    """Implementation of the Stock model."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='владелец')
    quantity = models.PositiveSmallIntegerField(default=0,
                                                validators = [MinValueValidator(0)], verbose_name='количество')
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2,
                                validators = [MinValueValidator(0.0)], verbose_name='стоимость')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f'{self.product.title} [{self.quantity}]'