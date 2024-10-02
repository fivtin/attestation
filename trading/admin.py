from django.contrib import admin

from trading.models import Supplier


# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'email', 'country',
                    'city', 'street', 'house',
                    'created_at', 'supplier', 'debt', )
    list_filter = ('user', 'country', 'city', )
