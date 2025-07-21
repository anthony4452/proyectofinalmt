# Aplicaciones/Equipos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipo, name='equipos'),  # /equipos/
    path('equipo', views.equipo),
    path('nuevoEquipo', views.nuevoEquipo),
    path('eliminarEquipo/<id>/', views.eliminarEquipo),
    path('editarEquipo/<id>/', views.editarEquipo),


    # CRUD ParticipacionEquipo
    path('participaciones/', views.lista_participaciones, name='lista_participaciones'),
    path('participaciones/nueva/', views.nueva_participacion, name='nueva_participacion'),
    path('participaciones/guardar/', views.guardar_participacion, name='guardar_participacion'),
    path('participaciones/editar/<int:id>/', views.editar_participacion, name='editar_participacion'),
    path('participaciones/guardarEdicion/<int:id>/', views.guardar_edicion_participacion, name='guardar_edicion_participacion'),
    path('participaciones/eliminar/<int:id>/', views.eliminar_participacion, name='eliminar_participacion'),
]
