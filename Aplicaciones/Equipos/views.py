# Aplicaciones/Jugadores/views.py
from django.shortcuts import render

def listaequipos(request):
    # lógica
    return render(request, 'equipos.html')
