from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from trading.models import Supplier
from trading.serializers import SupplierSerializer, SupplierUpdateSerializer, SupplierDetailSerializer, \
    SupplierCreateSerializer


# Create your views here.

class SupplierViewSet(ModelViewSet):
    """Set of views for implementing API with the Supplier model.
    Excluding the Debt field when changing via selecting a serializer class.
    Added filtering by the Country field.
    Access is restricted to authenticated users."""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', ]
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return SupplierUpdateSerializer
        elif self.action == 'retrieve':
            return SupplierDetailSerializer
        elif self.action == 'create':
            return SupplierCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        supplier = serializer.save(user=self.request.user)
        supplier.save()
