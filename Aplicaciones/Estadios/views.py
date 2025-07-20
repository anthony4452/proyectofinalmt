from django.shortcuts import render, redirect, get_object_or_404
from .models import Estadio
from .forms import EstadioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

# ✅ Función para verificar si el usuario es admin
def es_admin(user):
    return hasattr(user, 'perfilusuario') and user.perfilusuario.rol == 'admin'

# ✅ Solo el admin puede acceder a esta vista
@login_required
@user_passes_test(es_admin)
def estadio(request):
    estadios = Estadio.objects.all()
    return render(request, 'estadios.html', {'estadios': estadios})
    

@login_required
@user_passes_test(es_admin)
def editarEstadio(request, id):
    estadio = get_object_or_404(Estadio, id=id)
    if request.method == 'POST':
        form = EstadioForm(request.POST, instance=estadio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estadio editado correctamente.')
            return redirect('/estadios/')
    else:
        form = EstadioForm(instance=estadio)
    return render(request, 'editarEstadio.html', {'form': form, 'estadio': estadio})

@login_required
@user_passes_test(es_admin)
def nuevoEstadio(request):
    if request.method == 'POST':
        form = EstadioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estadio creado correctamente.')
            return redirect('/estadios/')
    else:
        form = EstadioForm()
    return render(request, 'nuevoEstadio.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def eliminarEstadio(request, id):
    estadio = get_object_or_404(Estadio, id=id)
    estadio.delete()
    messages.success(request, 'Estadio eliminado correctamente.')
    return redirect('/estadios/')
