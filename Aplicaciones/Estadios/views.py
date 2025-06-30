from django.shortcuts import render, redirect
from .models import Estadio
from .forms import EstadioForm
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def estadio (request):
    estadios = Estadio.objects.all()
    return render(request, 'estadios.html', {'estadios': estadios})

def editarEstadio(request, id):
    estadio = get_object_or_404(Estadio, id=id)  # Obtén el estadio por su ID
    if request.method == 'POST':
        form = EstadioForm(request.POST, instance=estadio)
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('/')  # Redirige a la lista de estadios
    else:
        form = EstadioForm(instance=estadio)  # Carga los datos existentes en el formulario
    return render(request, 'editarEstadio.html', {'form': form, 'estadio': estadio})

def nuevoEstadio(request):
    if request.method == 'POST':
        form = EstadioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirige a la lista de estadios
    else:
        form = EstadioForm()
    return render(request, 'nuevoEstadio.html', {'form': form})


def eliminarEstadio(request, id):
    estadio = Estadio.objects.get(id=id)
    estadio.delete()
    return redirect('/')
