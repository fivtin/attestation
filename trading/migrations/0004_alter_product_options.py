# Generated by Django 5.1.1 on 2024-10-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0003_alter_product_options_alter_stock_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукция'},
        ),
    ]
