from rest_framework import serializers
#Modelos
from .models.usuarios import Usuario
from .models.perfiles import Perfil
#Token de Rest Framework
from rest_framework.authtoken.models import Token

class UserSerializer (serializers.ModelSerializer):
    """
        Serializador que sirve para la obtención de datos de un usuario
    """
    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name','username', 'email', 'password', 'is_verified', 'is_superuser']
        extra_kwargs = {
            'password' : {'write_only': True}   
        }
    
    def create(self, validated_data):
        user = Usuario(
            first_name = validated_data['firs_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email'],
            is_verified = validated_data['is_verified'],
            is_superuser = validated_data['is_superuser'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user = user)
        
        return user

class ProfileSerializer (serializers.ModelSerializer):
    """
        Serializador de un perfil, que conserva la información de un usuario
    """
    usuario = UserSerializer(read_only = True)
    
    class Meta:
        model = Perfil
        fields = ['usuario', 'foto', 'genero', 'biografia', 'eventos_valorados']
        dept = 1