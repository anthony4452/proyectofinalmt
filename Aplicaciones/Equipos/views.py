from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo
from .forms import EquipoForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Función para validar si el usuario es admin
def es_admin(user):
    return hasattr(user, 'perfilusuario') and user.perfilusuario.rol == 'admin'

# Mostrar lista de equipos (solo admin)
@login_required
@user_passes_test(es_admin)
def equipo(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos.html', {'equipos': equipos})

# Crear nuevo equipo (solo admin)
@login_required
@user_passes_test(es_admin)
def nuevoEquipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/equipos/')
    else:
        form = EquipoForm()
    return render(request, 'nuevoEquipo.html', {'form': form})

# Editar equipo existente (solo admin)
@login_required
@user_passes_test(es_admin)
def editarEquipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('/equipos/')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'editarEquipo.html', {'form': form, 'equipo': equipo})
@login_required
@user_passes_test(es_admin)
def eliminarEquipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    return redirect('/equipos/')
