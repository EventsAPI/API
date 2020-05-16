from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .serializers import serializers
from .views import ReservacionViewSet
from django.urls import path, include


router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('Reservacion', ReservacionViewSet, basename='Reservacion')

urlpatterns = [
  path('', include(router.urls)),
]