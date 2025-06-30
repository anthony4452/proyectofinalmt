from django.shortcuts import render, redirect
from .models import Estadio

# Create your views here.

def estadio (request):
    estadios = Estadio.objects.all()
    return render(request, 'estadios.html', {'estadios': estadios})