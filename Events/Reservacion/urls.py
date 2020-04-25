from django.conf.urls.static import static

from rest_framework.router import DefaultRouter

from View import ReservacionView 

router =router.DefaultRouter()
 
router. register(' Reservacion', View.ReservacionView)


urlpatterns = [

    path('', include('router.urls')),
]