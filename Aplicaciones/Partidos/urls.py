# Aplicaciones/Partidos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_partidos, name='lista_partidos'),
    path('nuevo/', views.nuevo_partido, name='nuevo_partido'),
    path('guardar/', views.guardar_partido, name='guardar_partido'),
    path('editar/<int:id>/', views.editar_partido, name='editar_partido'),
    path('guardarEdicion/<int:id>/', views.guardar_edicion_partido, name='guardar_edicion_partido'),
    path('eliminar/<int:id>/', views.eliminar_partido, name='eliminar_partido'),
    path('posiciones/<int:temporada_id>/', views.ver_posiciones, name='ver_posiciones'),

]
