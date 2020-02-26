#Modelo que servirá para poder crear un Usuario Abstracto
from django.db import models
from django.conf import settings

class OwnerModel (models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True