"""Events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
#Para incluir las demás URL se utiliza el 'import include'

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Eventos.urls')), #URLs de Eventos
<<<<<<< HEAD
     path('', include('Reservacion.urls')),

=======
    path('', include('Usuarios.urls')), #URLs de Usuarios
    path('', include('Pagos.urls')), #URLs de Pagos
>>>>>>> 56e7d6177546dd29c66e175b5c191b1324d4214f
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
