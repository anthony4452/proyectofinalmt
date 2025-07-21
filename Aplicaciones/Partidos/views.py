from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Fecha, Partido
from Aplicaciones.Temporadas.models import Temporada
from Aplicaciones.Equipos.models import Equipo
# Create your views here.

# --- Partidos ---

def lista_partidos(request):
    partidos = Partido.objects.select_related('fecha', 'equipo_local', 'equipo_visitante').all()
    temporada = Temporada.objects.last()  # O la que necesites
    return render(request, 'lista.html', {'partidos': partidos, 'temporada': temporada})
def nuevo_partido(request):
    fechas = Fecha.objects.all()
    equipos = Equipo.objects.all()
    return render(request, 'nuevo.html', {'fechas': fechas, 'equipos': equipos})

def guardar_partido(request):
    if request.method == 'POST':
        fecha_id = request.POST.get('fecha')
        equipo_local_id = request.POST.get('equipo_local')
        equipo_visitante_id = request.POST.get('equipo_visitante')
        goles_local = request.POST.get('goles_local') or None
        goles_visitante = request.POST.get('goles_visitante') or None
        jugado = request.POST.get('jugado') == 'on'

        # Validación: local != visitante
        if equipo_local_id == equipo_visitante_id:
            messages.error(request, "El equipo local y visitante deben ser diferentes.")
            fechas = Fecha.objects.all()
            equipos = Equipo.objects.all()
            context = {
                'fechas': fechas,
                'equipos': equipos,
                'datos': request.POST,  # para mantener seleccionados los inputs
            }
            return render(request, 'nuevo.html', context)

        fecha = get_object_or_404(Fecha, id=fecha_id)
        equipo_local = get_object_or_404(Equipo, id=equipo_local_id)
        equipo_visitante = get_object_or_404(Equipo, id=equipo_visitante_id)

        partido = Partido(
            fecha=fecha,
            equipo_local=equipo_local,
            equipo_visitante=equipo_visitante,
            goles_local=goles_local,
            goles_visitante=goles_visitante,
            jugado=jugado
        )
        partido.save()
        messages.success(request, "Partido creado correctamente")
        return redirect('lista_partidos')
    return redirect('nuevo_partido')


def guardar_edicion_partido(request, id):
    if request.method == 'POST':
        partido = get_object_or_404(Partido, id=id)
        fecha_id = request.POST.get('fecha')
        equipo_local_id = request.POST.get('equipo_local')
        equipo_visitante_id = request.POST.get('equipo_visitante')
        goles_local = request.POST.get('goles_local') or None
        goles_visitante = request.POST.get('goles_visitante') or None
        jugado = request.POST.get('jugado') == 'on'

        # Validación: local != visitante
        if equipo_local_id == equipo_visitante_id:
            messages.error(request, "El equipo local y visitante deben ser diferentes.")
            fechas = Fecha.objects.all()
            equipos = Equipo.objects.all()
            context = {
                'partido': partido,
                'fechas': fechas,
                'equipos': equipos,
                'datos': request.POST,
            }
            return render(request, 'editar.html', context)

        partido.fecha = get_object_or_404(Fecha, id=fecha_id)
        partido.equipo_local = get_object_or_404(Equipo, id=equipo_local_id)
        partido.equipo_visitante = get_object_or_404(Equipo, id=equipo_visitante_id)
        partido.goles_local = goles_local
        partido.goles_visitante = goles_visitante
        partido.jugado = jugado
        partido.save()
        messages.success(request, "Partido actualizado correctamente")
        return redirect('lista_partidos')
    return redirect('editar_partido', id=id)

    if request.method == 'POST':
        fecha_id = request.POST.get('fecha')
        equipo_local_id = request.POST.get('equipo_local')
        equipo_visitante_id = request.POST.get('equipo_visitante')
        goles_local = request.POST.get('goles_local') or None
        goles_visitante = request.POST.get('goles_visitante') or None
        jugado = request.POST.get('jugado') == 'on'

        fecha = get_object_or_404(Fecha, id=fecha_id)
        equipo_local = get_object_or_404(Equipo, id=equipo_local_id)
        equipo_visitante = get_object_or_404(Equipo, id=equipo_visitante_id)

        partido = Partido(
            fecha=fecha,
            equipo_local=equipo_local,
            equipo_visitante=equipo_visitante,
            goles_local=goles_local,
            goles_visitante=goles_visitante,
            jugado=jugado
        )
        partido.save()
        messages.success(request, "Partido creado correctamente")
        return redirect('lista_partidos')
    return redirect('nuevo_partido')

def editar_partido(request, id):
    partido = get_object_or_404(Partido, id=id)
    fechas = Fecha.objects.all()
    equipos = Equipo.objects.all()
    return render(request, 'editar.html', {'partido': partido, 'fechas': fechas, 'equipos': equipos})


    if request.method == 'POST':
        partido = get_object_or_404(Partido, id=id)
        fecha_id = request.POST.get('fecha')
        equipo_local_id = request.POST.get('equipo_local')
        equipo_visitante_id = request.POST.get('equipo_visitante')
        goles_local = request.POST.get('goles_local') or None
        goles_visitante = request.POST.get('goles_visitante') or None
        jugado = request.POST.get('jugado') == 'on'

        partido.fecha = get_object_or_404(Fecha, id=fecha_id)
        partido.equipo_local = get_object_or_404(Equipo, id=equipo_local_id)
        partido.equipo_visitante = get_object_or_404(Equipo, id=equipo_visitante_id)
        partido.goles_local = goles_local
        partido.goles_visitante = goles_visitante
        partido.jugado = jugado
        partido.save()
        messages.success(request, "Partido actualizado correctamente")
        return redirect('lista_partidos')
    return redirect('editar_partido', id=id)

def eliminar_partido(request, id):
    partido = get_object_or_404(Partido, id=id)
    partido.delete()
    messages.success(request, "Partido eliminado correctamente")
    return redirect('lista_partidos')

# --- Posiciones (vista dinámica) ---

def ver_posiciones(request, temporada_id):
    temporada = get_object_or_404(Temporada, id=temporada_id)
    equipos = Equipo.objects.all()

    posiciones = []

    for equipo in equipos:
        partidos_local = Partido.objects.filter(fecha__temporada=temporada, equipo_local=equipo, jugado=True)
        partidos_visitante = Partido.objects.filter(fecha__temporada=temporada, equipo_visitante=equipo, jugado=True)

        pj = partidos_local.count() + partidos_visitante.count()
        ganados = empatados = perdidos = goles_favor = goles_contra = 0

        for p in partidos_local:
            goles_favor += p.goles_local or 0
            goles_contra += p.goles_visitante or 0
            if p.goles_local > p.goles_visitante:
                ganados += 1
            elif p.goles_local == p.goles_visitante:
                empatados += 1
            else:
                perdidos += 1

        for p in partidos_visitante:
            goles_favor += p.goles_visitante or 0
            goles_contra += p.goles_local or 0
            if p.goles_visitante > p.goles_local:
                ganados += 1
            elif p.goles_visitante == p.goles_local:
                empatados += 1
            else:
                perdidos += 1

        puntos = ganados * 3 + empatados
        diferencia = goles_favor - goles_contra

        posiciones.append({
            'equipo': equipo,
            'pj': pj,
            'ganados': ganados,
            'empatados': empatados,
            'perdidos': perdidos,
            'goles_favor': goles_favor,
            'goles_contra': goles_contra,
            'diferencia': diferencia,
            'puntos': puntos,
        })

    posiciones.sort(key=lambda x: (x['puntos'], x['diferencia'], x['goles_favor']), reverse=True)

    return render(request, 'listas.html', {
        'temporada': temporada,
        'posiciones': posiciones
    })