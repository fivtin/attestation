# Generated by Django 5.1.1 on 2024-10-04 11:59

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('model', models.CharField(max_length=128, verbose_name='модель')),
                ('launch_date', models.DateField(blank=True, null=True, verbose_name='дата начала продаж')),
                ('in_production', models.BooleanField(default=True, verbose_name='производится')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('country', models.CharField(max_length=128, verbose_name='страна')),
                ('city', models.CharField(max_length=128, verbose_name='город')),
                ('street', models.CharField(max_length=128, verbose_name='улица')),
                ('house', models.CharField(max_length=32, verbose_name='дом')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')),
                ('level', models.CharField(default='factory', max_length=10, verbose_name='уровень')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='задолженность')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trading.supplier', verbose_name='продавец')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'поставщик',
                'verbose_name_plural': 'поставщики',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='количество')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='стоимость')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.product', verbose_name='продукт')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.supplier', verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'склад',
                'verbose_name_plural': 'склады',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.supplier', verbose_name='производитель'),
        ),
    ]
