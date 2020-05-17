from django.urls import path, include
#Router
from rest_framework.routers import DefaultRouter
#Vista
from .views import PagosViewSet
from .views import RecibosViewSet

router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('pagos', PagosViewSet, basename='pagos')
router.register('recibos', RecibosViewSet, basename='recibos')

urlpatterns = [
  path('', include(router.urls)),
]