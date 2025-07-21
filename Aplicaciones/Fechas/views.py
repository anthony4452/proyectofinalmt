from django.shortcuts import render, redirect, get_object_or_404
from .models import Fecha
from django.contrib import messages
from Aplicaciones.Partidos.models import Partido
from Aplicaciones.Equipos.models import Equipo
from Aplicaciones.Temporadas.models import Temporada
# Fechas

def lista_fechas(request):
    fechas = Fecha.objects.all()
    return render(request, 'listaa.html', {'fechas': fechas})

def nueva_fecha(request):
    temporadas = Temporada.objects.all()
    return render(request, 'nuevaa.html', {'temporadas': temporadas})

def guardar_fecha(request):
    if request.method == 'POST':
        temporada_id = request.POST.get('temporada')
        numero = request.POST.get('numero')
        fecha_programada = request.POST.get('fecha_programada')

        # Validar duplicado
        if Fecha.objects.filter(temporada_id=temporada_id, numero=numero).exists():
            messages.error(request, f"La fecha número {numero} ya existe en esa temporada.")
            return redirect('nueva_fecha')  # o donde estés redirigiendo el form

        # Crear si no existe
        Fecha.objects.create(
            temporada_id=temporada_id,
            numero=numero,
            fecha_programada=fecha_programada
        )
        messages.success(request, "Fecha creada correctamente.")
        return redirect('lista_fechas')

def editar_fecha(request, id):
    fecha = get_object_or_404(Fecha, id=id)
    temporadas = Temporada.objects.all()
    return render(request, 'editaar.html', {'fecha': fecha, 'temporadas': temporadas})

def guardar_edicion_fecha(request, id):
    if request.method == 'POST':
        fecha = get_object_or_404(Fecha, id=id)
        temporada_id = request.POST.get('temporada')
        numero = request.POST.get('numero')
        fecha_programada = request.POST.get('fecha_programada')

        temporada = get_object_or_404(Temporada, id=temporada_id)

        fecha.temporada = temporada
        fecha.numero = numero
        fecha.fecha_programada = fecha_programada
        fecha.save()
        messages.success(request, "Fecha actualizada correctamente")
        return redirect('lista_fechas')
    else:
        return redirect('editar_fecha', id=id)

def eliminar_fecha(request, id):
    fecha = get_object_or_404(Fecha, id=id)
    fecha.delete()
    messages.success(request, "Fecha eliminada correctamente")
    return redirect('lista_fechas')
