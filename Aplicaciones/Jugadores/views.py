from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Jugador, InscripcionJugadores
from datetime import date
from Aplicaciones.Equipos.models import Equipo
from Aplicaciones.Temporadas.models import Temporada

def es_admin(user):
    return hasattr(user, 'perfilusuario') and user.perfilusuario.rol == 'admin'

@login_required
@user_passes_test(es_admin)
def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores.html', {'jugadores': jugadores})

@login_required
@user_passes_test(es_admin)
def nuevo_jugador(request):
    return render(request, 'nuevoJugador.html')

@login_required
@user_passes_test(es_admin)
def guardar_jugador(request):
    if request.method == "POST":
        nombres = request.POST.get("nombres")
        apellidos = request.POST.get("apellidos")
        nacimiento = request.POST.get("nacimiento")
        posicion = request.POST.get("posicion")
        foto = request.FILES.get("foto")
        cedula = request.POST.get("cedula")



        nuevo_jugador = Jugador.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            nacimiento=nacimiento,
            posicion=posicion,
            foto=foto,
            cedula=cedula
        )

        messages.success(request, "Jugador creado correctamente.")
        return redirect('jugadores')
    else:
        return redirect('nuevo_jugador')

@login_required
@user_passes_test(es_admin)
def editar_jugador(request, id):
    jugador = get_object_or_404(Jugador, pk=id)
    return render(request, 'editarJugador.html', {'jugador': jugador})

@login_required
@user_passes_test(es_admin)
def guardar_edicion_jugador(request, id):
    if request.method == "POST":
        jugador = get_object_or_404(Jugador, pk=id)

        jugador.nombres = request.POST.get("nombres")
        jugador.apellidos = request.POST.get("apellidos")
        jugador.nacimiento = request.POST.get("nacimiento")
        jugador.posicion = request.POST.get("posicion")
        jugador.cedula = request.POST.get("cedula")

        foto = request.FILES.get("foto")
        if foto:
            jugador.foto = foto

        jugador.save()

        messages.success(request, "Jugador actualizado correctamente.")
        return redirect('jugadores')
    else:
        return redirect('jugadores')

@login_required
@user_passes_test(es_admin)
def eliminar_jugador(request, id):
    jugador = get_object_or_404(Jugador, pk=id)
    jugador.delete()
    messages.success(request, "Jugador eliminado correctamente.")
    return redirect('jugadores')

@login_required
@user_passes_test(es_admin)
def detalle_equipo_temporada(request, equipo_id, temporada_id):
    from Aplicaciones.Equipos.models import Equipo
    from Aplicaciones.Temporadas.models import Temporada

    equipo = get_object_or_404(Equipo, pk=equipo_id)
    temporada = get_object_or_404(Temporada, pk=temporada_id)

    inscripciones = InscripcionJugadores.objects.filter(equipo=equipo, temporada=temporada).select_related('jugador')
    total_jugadores = inscripciones.count()

    context = {
        'equipo': equipo,
        'temporada': temporada,
        'jugadores': inscripciones,
        'total_jugadores': total_jugadores
    }
    return render(request, 'jugadores/detalles.html', context)


@login_required
@user_passes_test(es_admin)
def lista_inscripciones(request):
    inscripciones = InscripcionJugadores.objects.select_related('jugador', 'equipo', 'temporada').all()
    return render(request, 'inscripciones.html', {'inscripciones': inscripciones})

@login_required
@user_passes_test(es_admin)
def nueva_inscripcion(request):
    jugadores = Jugador.objects.all()
    equipos = Equipo.objects.all()
    temporadas = Temporada.objects.all()
    return render(request, 'nueva_inscripcion.html', {
        'jugadores': jugadores,
        'equipos': equipos,
        'temporadas': temporadas,
    })

@login_required
@user_passes_test(es_admin)
def guardar_inscripcion(request):
    if request.method == 'POST':
        jugador_id = request.POST.get('jugador')
        equipo_id = request.POST.get('equipo')
        temporada_id = request.POST.get('temporada')
        numero = request.POST.get('numero')

        # Validaciones básicas
        if not jugador_id or not equipo_id or not temporada_id or not numero:
            messages.error(request, 'Todos los campos son obligatorios')
            return redirect('nueva_inscripcion')

        # Verificar unicidad en modelo
        existe = InscripcionJugadores.objects.filter(
            jugador_id=jugador_id,
            temporada_id=temporada_id
        ).exists()

        if existe:
            messages.error(request, 'El jugador ya está inscrito en esta temporada')
            return redirect('nueva_inscripcion')

        existe_num = InscripcionJugadores.objects.filter(
            equipo_id=equipo_id,
            temporada_id=temporada_id,
            numero=numero
        ).exists()

        if existe_num:
            messages.error(request, 'El número ya está asignado en este equipo y temporada')
            return redirect('nueva_inscripcion')

        InscripcionJugadores.objects.create(
            jugador_id=jugador_id,
            equipo_id=equipo_id,
            temporada_id=temporada_id,
            numero=numero
        )
        messages.success(request, 'Inscripción creada correctamente')
        return redirect('lista_inscripciones')

@login_required
@user_passes_test(es_admin)
def editar_inscripcion(request, id):
    inscripcion = get_object_or_404(InscripcionJugadores, pk=id)
    jugadores = Jugador.objects.all()
    equipos = Equipo.objects.all()
    temporadas = Temporada.objects.all()
    return render(request, 'editar_inscripcion.html', {
        'inscripcion': inscripcion,
        'jugadores': jugadores,
        'equipos': equipos,
        'temporadas': temporadas,
    })

@login_required
@user_passes_test(es_admin)
def guardar_edicion_inscripcion(request, id):
    if request.method == 'POST':
        inscripcion = get_object_or_404(InscripcionJugadores, pk=id)

        jugador_id = request.POST.get('jugador')
        equipo_id = request.POST.get('equipo')
        temporada_id = request.POST.get('temporada')
        numero = request.POST.get('numero')

        # Validaciones iguales que al crear (salvo que ignore la propia)
        if not jugador_id or not equipo_id or not temporada_id or not numero:
            messages.error(request, 'Todos los campos son obligatorios')
            return redirect('editar_inscripcion', id=id)

        existe = InscripcionJugadores.objects.filter(
            jugador_id=jugador_id,
            temporada_id=temporada_id
        ).exclude(pk=id).exists()

        if existe:
            messages.error(request, 'El jugador ya está inscrito en esta temporada')
            return redirect('editar_inscripcion', id=id)

        existe_num = InscripcionJugadores.objects.filter(
            equipo_id=equipo_id,
            temporada_id=temporada_id,
            numero=numero
        ).exclude(pk=id).exists()

        if existe_num:
            messages.error(request, 'El número ya está asignado en este equipo y temporada')
            return redirect('editar_inscripcion', id=id)

        inscripcion.jugador_id = jugador_id
        inscripcion.equipo_id = equipo_id
        inscripcion.temporada_id = temporada_id
        inscripcion.numero = numero
        inscripcion.save()
        messages.success(request, 'Inscripción actualizada correctamente')
        return redirect('lista_inscripciones')

@login_required
@user_passes_test(es_admin)
def eliminar_inscripcion(request, id):
    inscripcion = get_object_or_404(InscripcionJugadores, pk=id)
    inscripcion.delete()
    messages.success(request, 'Inscripción eliminada correctamente')
    return redirect('lista_inscripciones')