from rest_framework.routers import DefaultRouter

from trading.apps import TradingConfig
from trading.views import SupplierViewSet

app_name = TradingConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='suppliers')


urlpatterns =  router.urls
