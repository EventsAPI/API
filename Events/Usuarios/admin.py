from django.contrib import admin

# Registrando modelos
from .models.usuarios import Usuario
from .models.perfiles import Perfil

@admin.register (Perfil)
class Perfil (admin.ModelAdmin):
    list_display = ('usuario', 'foto', 'genero', 'biografia',)
    list_filter = ('usuario', 'genero',)

@admin.register (Usuario)
class Usuario (admin.ModelAdmin):
    list_display = ('username', 'email', 'is_verified',)
    list_filter = ('is_verified',)
