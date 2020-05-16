from django.urls import path, include
#Vistas
from .views import UsuarioViewSet, LoginView
#Para el Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login')
]
