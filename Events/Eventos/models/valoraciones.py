from django.db import models
from models  import Valoraciones


class Valoraciones (models.Model):
    Valoraciones = models.FloatField()    
    idUsuario = models.ForeignKey('Usuarios.Usuario', on_delete=models.DO_NOTHING)

    nombre = models.CharField(max_length=50)
    evento = models.CharField (max_length= 50 )       
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=255)
    
    idLocalidad = models.ForeignKey('Eventos.Localidad', on_delete=models.DO_NOTHING)