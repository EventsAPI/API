from django.db import models

class Valoraciones (models.Model):
    valoracion = models.FloatField()
    evento = models.ForeignKey('Eventos.Eventos', related_name='eventosVal', null=True, blank=True, on_delete=models.CASCADE)