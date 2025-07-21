from django.urls import path
from . import views

urlpatterns = [
    # Jugadores
    path('', views.jugadores, name='jugadores'),  # Lista todos los jugadores
    path('nuevo/', views.nuevo_jugador, name='nuevo_jugador'),
    path('guardar/', views.guardar_jugador, name='guardar_jugador'),
    path('editar/<int:id>/', views.editar_jugador, name='editar_jugador'),
    path('guardarEdicion/<int:id>/', views.guardar_edicion_jugador, name='guardar_edicion_jugador'),
    path('eliminar/<int:id>/', views.eliminar_jugador, name='eliminar_jugador'),

    # Detalle equipo-temporada con inscripciones filtradas
    path('inscripciones/<int:equipo_id>/<int:temporada_id>/', views.detalle_equipo_temporada, name='detalle_equipo_temporada'),

    # Inscripciones
    path('inscripciones/', views.lista_inscripciones, name='lista_inscripciones'),  # Lista todas las inscripciones
    path('inscripciones/nueva/', views.nueva_inscripcion, name='nueva_inscripcion'),
    path('inscripciones/guardar/', views.guardar_inscripcion, name='guardar_inscripcion'),
    path('inscripciones/editar/<int:id>/', views.editar_inscripcion, name='editar_inscripcion'),
    path('inscripciones/guardarEdicion/<int:id>/', views.guardar_edicion_inscripcion, name='guardar_edicion_inscripcion'),
    path('inscripciones/eliminar/<int:id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]
