from django.contrib import admin

from trading.models import Supplier, Product


# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'email', 'country',
                    'city', 'street', 'house',
                    'created_at', 'supplier', 'debt', )
    list_filter = ('user', 'country', 'city', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'launch_date', )
    search_fields = ('title', )
