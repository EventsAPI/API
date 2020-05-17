from django.db import models
from django.conf import settings

class Valoraciones (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_v', on_delete=models.SET_NULL, blank=True, null=True)
    valoracion = models.FloatField()
