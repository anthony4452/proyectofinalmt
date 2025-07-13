# Aplicaciones/Jugadores/views.py
from django.shortcuts import render

def lista_jugadores(request):
    # lógica
    return render(request, 'jugadores/lista.html')
