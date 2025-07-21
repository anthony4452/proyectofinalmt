from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from Aplicaciones.Jugadores.models import Jugador, InscripcionJugadores
from Aplicaciones.Equipos.models import Equipo
from Aplicaciones.Temporadas.models import Temporada
from .models import Traspaso

def vista_traspasos(request):
    jugadores = Jugador.objects.all()
    equipos = Equipo.objects.all()
    traspasos = Traspaso.objects.select_related('jugador', 'desde_equipo', 'hacia_equipo', 'temporada_origen')

    return render(request, 'traspasos.html', {
        'jugadores': jugadores,
        'equipos': equipos,
        'traspasos': traspasos
    })

def gestionar_traspaso(request):
    if request.method == 'POST':
        jugador_id = request.POST.get('jugador')
        hacia_equipo_id = request.POST.get('hacia_equipo')

        jugador = get_object_or_404(Jugador, id=jugador_id)
        inscripcion = InscripcionJugadores.objects.filter(jugador=jugador).order_by('-temporada__id').first()

        if not inscripcion:
            return JsonResponse({'success': False, 'message': 'El jugador no tiene una inscripción registrada.'})

        temporada = inscripcion.temporada

        if int(hacia_equipo_id) == inscripcion.equipo.id:
            return JsonResponse({'success': False, 'message': 'No puedes traspasar al mismo equipo.'})

        ya_traspasado = Traspaso.objects.filter(jugador=jugador, temporada_origen=temporada).exists()
        if ya_traspasado:
            return JsonResponse({'success': False, 'message': 'Este jugador ya fue traspasado esta temporada.'})

        traspaso = Traspaso.objects.create(
            jugador=jugador,
            desde_equipo=inscripcion.equipo,
            hacia_equipo_id=hacia_equipo_id,
            temporada_origen=temporada,
            fecha_traspaso=timezone.now().date()
        )

        return JsonResponse({
            'success': True,
            'message': 'Traspaso realizado con éxito.',
            'traspaso': {
                'jugador': f'{jugador.nombres} {jugador.apellidos}',
                'desde_equipo': traspaso.desde_equipo.nombre,
                'hacia_equipo': traspaso.hacia_equipo.nombre,
                'temporada': str(temporada),
                'fecha': traspaso.fecha_traspaso.strftime('%d/%m/%Y')
            }
        })
