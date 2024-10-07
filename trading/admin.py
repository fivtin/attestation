from django.contrib import admin

from trading.models import Supplier, Product, Stock


# Register your models here.


@admin.action(description="Remove debt from vendors.")
def make_remove_debt(modeladmin, request, queryset):
    """Action for admin-panel: Remove debt to vendor. Set debt = 0. """
    queryset.update(debt=0)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Model Supplier for admin panel."""

    list_display = ('id', 'user', 'title', 'email', 'country',
                    'city', 'street', 'house',
                    'created_at', 'level', 'vendor', 'debt', )
    list_filter = ('user', 'country', 'city', )
    search_fields = ('title', )
    actions = [make_remove_debt]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Model Product for admin panel."""

    list_display = ('id', 'title', 'model', 'launch_date', )
    search_fields = ('title', )


@admin.register(Stock)
class ProductAdmin(admin.ModelAdmin):
    """Model Stock for admin panel."""

    list_display = ('id', 'product', 'supplier', 'quantity', 'price', )
    search_fields = ('product', 'supplier', )
