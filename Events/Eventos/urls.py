from django.urls import path
from .views import CrearEvento, ListarEvento, BorrarEvento, ActualizarEvento, CrearValoracion, MostrarValoracion


urlpatterns = [
    path('evento/crear', CrearEvento.as_view(), name = 'crearEvento'),
    path('evento/mostrar/', ListarEvento.as_view(), name = 'listarEvento'),
    path('evento/borrar/', BorrarEvento.as_view(), name = 'borrarEvento'),
    path('evento/actualizar/', ActualizarEvento.as_view(), name = 'actualizarEvento'),    
    path('valoraciones/crear', CrearValoracion.as_view(), name = 'crearvaloracion '),
    path('valoraciones/mostrar ', MostrarValoracion.as_view(), name = 'mostrarvaloracion'),

]
