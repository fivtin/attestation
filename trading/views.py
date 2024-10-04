from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from trading.models import Supplier
from trading.serializers import SupplierSerializer, SupplierUpdateSerializer


# Create your views here.

class SupplierViewSet(ModelViewSet):

    serializer_class = SupplierSerializer
    queryset =Supplier.objects.all()
    # permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return SupplierUpdateSerializer
        return self.serializer_class