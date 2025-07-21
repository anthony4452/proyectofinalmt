from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fechas, name='lista_fechas'),
    path('nueva/', views.nueva_fecha, name='nueva_fecha'),
    path('guardar/', views.guardar_fecha, name='guardar_fecha'),
    path('editar/<int:id>/', views.editar_fecha, name='editar_fecha'),
    path('guardarEdicion/<int:id>/', views.guardar_edicion_fecha, name='guardar_edicion_fecha'),
    path('eliminar/<int:id>/', views.eliminar_fecha, name='eliminar_fecha'),
]
