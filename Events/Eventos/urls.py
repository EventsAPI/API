from django.urls import path, include
#vistas Evento
from .views.eventos import CrearEvento, ListarEvento, BorrarEvento, ActualizarEvento, ListarDepartamento
#vistas generales del módulo
from .views.localidades import AsientosViewSet, CrearLocalidad, ListarLocalidad, MostrarLocalidad, ActualizarLocalidad, BorrarLocalidad
from .views.comentarios import ComentariosViewSet
from .views.valoraciones import ValoracionesViewSet

#Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('asientos', AsientosViewSet, basename='asientos')
router.register('comentarios', ComentariosViewSet, basename='comentarios')
router.register('valoraciones', ValoracionesViewSet, basename='valoraciones')

urlpatterns = [
    path('evento/crear', CrearEvento.as_view(), name = 'crearEvento'),
    path('evento/mostrar/', ListarEvento.as_view(), name = 'listarEvento'),
    path('evento/mostrar/<lugar>', ListarDepartamento.as_view(), name = 'listarDepartamento'),
    path('evento/borrar/<pk>', BorrarEvento.as_view(), name = 'borrarEvento'),
    path('evento/actualizar/<pk>', ActualizarEvento.as_view(), name = 'actualizarEvento'),
    #URLs localidades
    path('localidad/crear', CrearLocalidad.as_view(), name = 'crearLocalidad'),
    path('localidad/listar/', ListarLocalidad.as_view(), name = 'listarLocalidad'),
    path('localidad/listar/<pk>', MostrarLocalidad.as_view(), name = 'mostrarLocalidad'),
    path('localidad/actualizar/<pk>', ActualizarLocalidad.as_view(), name = 'actualizarLocalidad'),
    path('localidad/borrar/<pk>', BorrarLocalidad.as_view(), name = 'borrarLocalidad'),
    path('', include(router.urls)),
]
