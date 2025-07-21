from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, ParticipacionEquipo
from Aplicaciones.Temporadas.models import Temporada
from .forms import EquipoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


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
            messages.success(request, 'Equipo creado correctamente.')
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
            messages.success(request, 'Equipo actualizado correctamente.')
            return redirect('/equipos/')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'editarEquipo.html', {'form': form, 'equipo': equipo})
@login_required
@user_passes_test(es_admin)
def eliminarEquipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    messages.success(request, 'Equipo eliminado correctamente.')
    return redirect('/equipos/')



def lista_participaciones(request):
    participaciones = ParticipacionEquipo.objects.select_related('equipo', 'temporada').all()
    return render(request, 'lista_participaciones.html', {'participaciones': participaciones})

def nueva_participacion(request):
    equipos = Equipo.objects.all()
    temporadas = Temporada.objects.all()
    return render(request, 'nueva_participacion.html', {'equipos': equipos, 'temporadas': temporadas})

def guardar_participacion(request):
    if request.method == "POST":
        equipo_id = request.POST.get('equipo')
        temporada_id = request.POST.get('temporada')

        # Validar que no exista ya la combinación (por unique_together)
        existe = ParticipacionEquipo.objects.filter(equipo_id=equipo_id, temporada_id=temporada_id).exists()
        if existe:
            messages.error(request, 'Esta participación ya está registrada.')
            return redirect('nueva_participacion')

        participacion = ParticipacionEquipo.objects.create(
            equipo_id=equipo_id,
            temporada_id=temporada_id,
        )
        messages.success(request, 'Participación registrada correctamente.')
        return redirect('lista_participaciones')
    else:
        return redirect('lista_participaciones')

def editar_participacion(request, id):
    participacion = get_object_or_404(ParticipacionEquipo, pk=id)
    equipos = Equipo.objects.all()
    temporadas = Temporada.objects.all()
    return render(request, 'editar_participacion.html', {
        'participacion': participacion,
        'equipos': equipos,
        'temporadas': temporadas
    })

def guardar_edicion_participacion(request, id):
    if request.method == "POST":
        equipo_id = request.POST.get('equipo')
        temporada_id = request.POST.get('temporada')

        participacion = get_object_or_404(ParticipacionEquipo, pk=id)

        # Validar que no exista otro registro con la misma combinación
        existe = ParticipacionEquipo.objects.filter(
            equipo_id=equipo_id, temporada_id=temporada_id
        ).exclude(pk=id).exists()
        if existe:
            messages.error(request, 'Otra participación con este equipo y temporada ya existe.')
            return redirect('editar_participacion', id=id)

        participacion.equipo_id = equipo_id
        participacion.temporada_id = temporada_id
        participacion.save()
        messages.success(request, 'Participación actualizada correctamente.')
        return redirect('lista_participaciones')
    else:
        return redirect('lista_participaciones')

def eliminar_participacion(request, id):
    participacion = get_object_or_404(ParticipacionEquipo, pk=id)
    participacion.delete()
    messages.success(request, 'Participación eliminada correctamente.')
    return redirect('lista_participaciones')