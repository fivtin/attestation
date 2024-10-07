from django.core.serializers import serialize
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from trading.models import Supplier, Product


class ProductSerializer(ModelSerializer):
    """Serialization of all Product fields."""
    class Meta:
        model = Product
        fields = '__all__'


class SupplierSerializer(ModelSerializer):
    """Serialization of all Supplier fields on output."""
    products = SerializerMethodField(read_only=True)

    class Meta:
        model = Supplier
        fields = '__all__'

    def get_products(self, instance):
        queryset = Product.objects.filter(supplier=instance).all()
        return ProductSerializer(queryset, many=True).data


class SupplierUpdateSerializer(SupplierSerializer):
    """Serialization of all Supplier fields (except the debt field) when editing."""
    class Meta:
        model = Supplier
        exclude= ('debt', )
