#Modelo que servirá para poder crear un Usuario Abstracto
from django.db import models
from django.conf import settings

class OwnerModel (models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

class InicioModel (models.Model):
    creado = models.DateTimeField(
        'creado el', auto_now_add=True, help_text='Fecha en la que se registró.'
    )
    modificado = models.DateTimeField(
        'modificado el', auto_now=True, help_text='Fecha en la que se modificó.'
    )
    
    class Meta:
        abstract=True