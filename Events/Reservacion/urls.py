from django.conf.urls.static import static
from api import View 

router =router.DefaultRouter()
 
router. register(' Reservacion', View.ReservacionView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('router.urls')),
]