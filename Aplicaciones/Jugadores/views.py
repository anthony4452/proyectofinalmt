# Aplicaciones/Jugadores/views.py
from django.shortcuts import render
from .models import Jugador, InscripcionJugadores
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def jugadores(request):
    listajugadores = Jugador.objects.all()
    return render(request, 'jugadores.html', {'listajugadores': listajugadores})

def nuevoJugador(request):
    return render(request, 'nuevoJugador.html')

