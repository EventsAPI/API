
from django.urls import path, include
from .serializers.pagos import PagosSerializer
from rest_framework.routers import DefaultRouter
from Pagos import views
from .views import PagosViewSet



router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('Pagos', PagosViewSet, basename='Pagos' )

urlpatterns = [
  path('', include(router.urls)),
]