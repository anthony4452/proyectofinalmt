# Aplicaciones/Equipos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipo, name='equipos'),  # /equipos/
    path('equipo', views.equipo),
    path('nuevoEquipo', views.nuevoEquipo),
    path('eliminarEquipo/<id>/', views.eliminarEquipo),
    path('editarEquipo/<id>/', views.editarEquipo),
]
