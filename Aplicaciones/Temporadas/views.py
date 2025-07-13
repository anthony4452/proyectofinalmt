from django.shortcuts import render, redirect, get_object_or_404
from .models import Temporada

def temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, 'temporadas.html', {'temporadas': temporadas})


def nuevaTemporada(request):
    return render(request, 'nuevaTemporada.html')