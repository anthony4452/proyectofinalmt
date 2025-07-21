from django.shortcuts import render, redirect, get_object_or_404
from Aplicaciones.Jugadores.models import Jugador
from .models import Carnet
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.views.decorators.http import require_POST


def generar_qr_para_jugador(jugador):
    ultima_inscripcion = InscripcionJugadores.objects.filter(jugador=jugador).order_by('-temporada__id').first()
    equipo_nombre = ultima_inscripcion.equipo.nombre if ultima_inscripcion else "Sin equipo"

    datos = f"Nombre: {jugador.nombres} {jugador.apellidos}\nEquipo: {equipo_nombre}\nDNI: {jugador.cedula}"

    qr = qrcode.make(datos)
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    filename = f'qr_jugador_{jugador.id}.png'

    carnet, created = Carnet.objects.get_or_create(jugador=jugador)
    if not carnet.qr_code:
        carnet.qr_code.save(filename, ContentFile(buffer.getvalue()), save=True)
    return carnet
from Aplicaciones.Jugadores.models import Jugador, InscripcionJugadores

def jugcarnet(request):
    jugadores = Jugador.objects.all()

    for jugador in jugadores:
        ultima_inscripcion = InscripcionJugadores.objects.filter(jugador=jugador).order_by('-temporada__id').first()
        jugador.nombre_equipo = ultima_inscripcion.equipo.nombre if ultima_inscripcion else 'Sin equipo'

    carnets = Carnet.objects.select_related('jugador').all()  # Trae todos los carnets con sus jugadores

    context = {
        'jugadores': jugadores,
        'carnets': carnets,  # Aquí agregas los carnets
    }
    return render(request, 'jugcarnets.html', context)

@require_POST
def generar_carnet(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    generar_qr_para_jugador(jugador)
    # Luego rediriges a la lista o donde quieras
    return redirect('carnets:jugcarnet')
