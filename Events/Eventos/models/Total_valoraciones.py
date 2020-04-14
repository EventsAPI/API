from django.db import models

class Total_valoraciones (models.Model):

    fecha = models.DateTimeField()
    comentario = models.TextField(max_length=500, blank=True)
    idUsuario = models.ForeignKey('Usuarios.Usuario', on_delete=models.DO_NOTHING)
