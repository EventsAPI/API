from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario (AbstractUser):
    username = models.CharField(
        'username',
        max_length = 50,
        unique = True,
        error_messages = {
            'unique': 'Ya existe un usuario con este nombre de usuario.'
        }
    )
    
    USERNAME_FIELD = 'username'
    
    email = models.EmailField(
        'email_address',
        unique = True,
        error_messages = {
            'unique': 'Ya existe un usuario con ese correo.'
        }
    )
    
    is_superuser = models.BooleanField(
        'administrador',
        default=False,
        help_text='Verdadero si el usuario es un administrador del sitio.'
    )
    
    is_verified = models.BooleanField(
        'usuario', 
        default=True, 
        help_text='Verdadero si el usuario verificó su registro.'
    )
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username