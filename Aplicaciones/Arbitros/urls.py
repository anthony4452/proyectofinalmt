from django.urls import path
from . import views

urlpatterns = [
    path('', views.arbitros , name='inicio_arbitros'),
    path('arbitros', views.arbitros),
    path('nuevoArbitro', views.nuevoArbitro),
    path('eliminarArbitro/<id>/', views.eliminarArbitro),
    path('editarArbitro/<id>/', views.editarArbitro),
]
