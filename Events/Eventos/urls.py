from django.urls import path
from .views import CrearEvento, ListarEvento, BorrarEvento, ActualizarEvento

urlpatterns = [
    path('evento/crear', CrearEvento.as_view(), name = 'crearEvento'),
    path('evento/mostrar/', ListarEvento.as_view(), name = 'listarEvento'),
    path('evento/borrar/<pk>', BorrarEvento.as_view(), name = 'borrarEvento'),
    path('evento/actualizar/<pk>', ActualizarEvento.as_view(), name = 'actualizarEvento')
]
