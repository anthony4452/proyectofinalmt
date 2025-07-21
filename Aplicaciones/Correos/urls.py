from django.urls import path
from . import views

urlpatterns = [
    path('correos/', views.correos_list, name='correos_list'),
    path('correos/form/', views.correos_form, name='correos_form'),
    path('correos/form/<int:id_editar>/', views.correos_form, name='editar_correo'),
    path('correos/eliminar/<int:id>/', views.eliminar_correo, name='eliminar_correo'),
    path('correos/enviar/<int:id>/', views.enviar_correo, name='enviar_correo'),
]
