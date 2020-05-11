from django.conf.urls.static import static
from rest_framework.router import DefaultRouter
from .serializers import ReservacionSerializer
from .view import ReservacionViewSet

router = DefaultRouter()
 
router.register('Reservacion', ReservacionViewSet, basename='Reservacion')
urlpatterns = [

    path('', include('router.urls')),
]