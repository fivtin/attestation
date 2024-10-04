from django.contrib import admin

from trading.models import Supplier, Product, Stock


# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'email', 'country',
                    'city', 'street', 'house',
                    'created_at', 'level', 'seller', 'debt', )
    list_filter = ('user', 'country', 'city', )
    search_fields = ('title', )
    # filter_horizontal = ('products', )



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'launch_date', )
    search_fields = ('title', )


@admin.register(Stock)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'supplier', 'quantity', 'price', )
    search_fields = ('product', 'supplier', )
