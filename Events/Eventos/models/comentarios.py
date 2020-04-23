from django.db import models

class Comentarios (models.Model):
    fecha = models.DateTimeField()
    comentario = models.TextField(max_length=500, blank=True)
    
    evento = models.ForeignKey('Eventos.Eventos', related_name='eventosComent', null=True, blank=True, on_delete=models.CASCADE)