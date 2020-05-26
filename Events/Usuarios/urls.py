from django.urls import path, include
#Vistas
from .views import CrearUsuario, ListarUsuarios, ActualizarUsuario, EliminarUsuario, VerUsuario, LoginView, VerPerfiles, VerActualizarPerfil, VerPerfil

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    #URL de Usuarios
    path('usuarios/crear/', CrearUsuario.as_view(), name='crearUsuario'),
    path('usuarios/listar/', ListarUsuarios.as_view(), name='listarUsuarios'),
    path('usuarios/actualizar/<pk>', ActualizarUsuario.as_view(), name='actualizarUsuario'),
    path('usuarios/eliminar/<pk>', EliminarUsuario.as_view(), name='eliminarUsuario'),
    path('usuarios/ver/<pk>', VerUsuario.as_view(), name='verUsuario'),
    #URLs de Perfiles
    path('usuarios/perfil/usuarioActual/', VerActualizarPerfil.as_view(), name='perfilUsuario'),
    path('usuarios/perfiles/general/', VerPerfiles.as_view(), name='perfiles'),
    path('usuarios/perfil/<pk>', VerPerfil.as_view(), name='verPerfil'),
]
