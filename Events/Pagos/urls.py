from django.urls import path, include
#Serializador
from .serializers.pagos import PagosSerializer
#Router
from rest_framework.routers import DefaultRouter
#Vista
from .views import PagosViewSet

router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('pagos', PagosViewSet, basename='pagos')

urlpatterns = [
  path('', include(router.urls)),
]