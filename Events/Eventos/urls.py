
from django.urls import path, include
from .serializers.eventos import EventosSerializer
from rest_framework.routers import DefaultRouter
from Eventos import views
from .views import EventosViewSet



router = DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('Eventos', EventosViewSet, basename='Eventos' )

urlpatterns = [
  path('', include(router.urls)),
]