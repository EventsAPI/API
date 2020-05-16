from rest_framework import serializers
#Modelos
from .models.usuarios import Usuario
from .models.perfiles import Perfil
#Token de Rest Framework
from rest_framework.authtoken.models import Token

class ProfileSerializer (serializers.ModelSerializer):
    """
        Serializador de un perfil, que conserva la información de un usuario
    """
    class Meta:
        model = Perfil
        fields = ['usuario', 'foto', 'creado', 'genero', 'biografia']
        read_only_fields = ['eventos_valorados']

class UserSerializer (serializers.ModelSerializer):
    """
        Serializador que sirve para la obtención de datos de un usuario
    """
    perfil = ProfileSerializer(read_only = True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name','username', 'email', 'password', 'is_superuser', 'perfil']
        extra_kwargs = {
            'password' : {'write_only': True}   
        }
        depth = 1
    
    def create(self, validated_data):
        user = Usuario(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email'],
            is_superuser = validated_data['is_superuser'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        
        biografia_default = 'Aun no tiene biografia completa.'
        Perfil.objects.create(usuario = user, biografia= biografia_default)
        
        return user