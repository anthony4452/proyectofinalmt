# Ejemplo: Aplicaciones/Jugadores/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.jugadores, name='jugadores'),
    # otras rutas...
]
