from django.db import models
from Eventos.models.valoraciones import Valoraciones
from .views import CrearValoracion, MostrarValoracion


class Valoraciones (models.Model):
    valoracion = models.FloatField()    
    idUsuario = models.ForeignKey('Usuarios.Usuario', on_delete=models.DO_NOTHING)

    nombre = models.CharField(max_length=50)
    evento = models.CharField (max_length= 50 )       
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=255)
    
    idLocalidad = models.ForeignKey('Eventos.Localidad', on_delete=models.DO_NOTHING)