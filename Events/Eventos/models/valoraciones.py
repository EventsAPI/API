from django.db import models

class Valoraciones (models.Model):
    valoracion = models.FloatField()
    
    idUsuario = models.ForeignKey('Usuarios.Usuario', on_delete=models.DO_NOTHING)