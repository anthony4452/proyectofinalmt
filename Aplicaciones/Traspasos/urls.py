from django.urls import path
from . import views

app_name = 'traspasos'

urlpatterns = [
    path('', views.vista_traspasos, name='listar'),
    path('realizar/', views.gestionar_traspaso, name='realizar'),
]
