from django.urls import path, include
#vistas Evento
from .views.eventos import CrearEvento, ListarEvento, BorrarEvento, ActualizarEvento
#vistas Localidad
from .views.localidades import LocalidadViewSet

#Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('localidad', LocalidadViewSet, basename='localidad')


urlpatterns = [
    path('evento/crear', CrearEvento.as_view(), name = 'crearEvento'),
    path('evento/mostrar/', ListarEvento.as_view(), name = 'listarEvento'),
    path('evento/borrar/<pk>', BorrarEvento.as_view(), name = 'borrarEvento'),
    path('evento/actualizar/<pk>', ActualizarEvento.as_view(), name = 'actualizarEvento'),
    path('', include(router.urls)),
]
