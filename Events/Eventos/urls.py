from django.urls import path
from .views import CrearEvento, ListarEvento, BorrarEvento, ActualizarEvento

urlpatterns = [
    path('evento/crear', CrearEvento.as_view(), basename = 'crearEvento'),
    path('evento/mostrar/', ListarEvento.as_view(), basename = 'listarEvento'),
    path('evento/borrar/', BorrarEvento.as_view(), basename = 'borrarEvento'),
    path('evento/actualizar/', ActualizarEvento.as_view(), basename = 'actualizarEvento')
]
