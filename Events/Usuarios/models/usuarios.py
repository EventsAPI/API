from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario (AbstractUser):
    
    USERNAME_FIELD = 'username'
    
    is_verified = models.BooleanField(
        'usuario', default=True, help_text='Verdadero si el usuario verificó su registro.'
    )
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username