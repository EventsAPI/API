from django.urls import path, include
from .Serializers.pagos import PagosSerializer
from rest_framework.routers import DefaultRouter
from pagos import views
from .views import PagosViewSet



router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('Pagos', EventosViewSet, basename='Pagos' )
router.register('Recibos', EventosViewSet, basename='Recibos' )

urlpatterns = [
  path('', include(router.urls)),
]