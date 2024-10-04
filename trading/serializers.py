from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from trading.models import Supplier, Product


class SupplierSerializer(ModelSerializer):
    products = SerializerMethodField()

    class Meta:
        model = Supplier
        fields = '__all__'

    def get_products(self, instance):
        return Product.objects.filter(supplier=instance).all()


class SupplierUpdateSerializer(SupplierSerializer):
    class Meta:
        model = Supplier
        exclude= ('debt', )