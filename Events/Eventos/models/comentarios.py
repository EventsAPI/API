from django.db import models
from django.conf import settings

class Comentarios (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.SET_NULL, blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True)
    comentario = models.TextField(max_length=500, blank=True)