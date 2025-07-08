from django.shortcuts import render, redirect, get_object_or_404
from .models import Temporada
from .forms import TemporadaForm
def lista_temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, 'lista.html', {'temporadas': temporadas})

def crear_temporada(request):
    if request.method == 'POST':
        form = TemporadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_temporadas')
    else:
        form = TemporadaForm()
    return render(request, 'form.html', {'form': form})

def editar_temporada(request, pk):
    temporada = get_object_or_404(Temporada, pk=pk)
    if request.method == 'POST':
        form = TemporadaForm(request.POST, instance=temporada)
        if form.is_valid():
            form.save()
            return redirect('lista_temporadas')
    else:
        form = TemporadaForm(instance=temporada)
    return render(request, 'form.html', {'form': form})

def eliminar_temporada(request, pk):
    temporada = get_object_or_404(Temporada, pk=pk)
    if request.method == 'POST':
        temporada.delete()
        return redirect('lista_temporadas')
    return render(request, 'confirmar_eliminar.html', {'temporada': temporada})
