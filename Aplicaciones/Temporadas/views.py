from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Temporada
from django.http import FileResponse


def ver_pdf(request, id):
    reglamento = get_object_or_404(Temporada, pk=id)
    return FileResponse(reglamento.reglamento.open(), content_type='application/pdf')



def temporadas(request):
    temporadas = Temporada.objects.all()
    return render(request, 'temporadas.html', {'temporadas': temporadas})


def nuevaTemporada(request):
    return render(request, 'nuevaTemporada.html')

def guardarTemporada(request):
    if request.method == "POST":
        nombreliga = request.POST.get("nombreliga")
        nombretorneo = request.POST.get("nombretorneo")
        año = request.POST.get("año")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        reglamento = request.FILES.get("reglamento")

        # Aquí deberías validar que no sean None ni vacíos

        nuevoReglamento = Temporada.objects.create(
            nombreliga=nombreliga,
            nombretorneo=nombretorneo,
            año=año,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            reglamento=reglamento
        )

        messages.success(request, "Se ha guardado la temporada correctamente")
        return redirect('/temporadas')
    else:
        # Podrías mostrar un error o redirigir
        return redirect('/temporadas/nuevaTemporada/')
    

def editarTemporada(request, id):
    editarTemporada = Temporada.objects.get(pk=id)
    return render(request, 'editarTemporada.html', {'temporada': editarTemporada})

def guardarEdicionTemporada(request, id):
    if request.method == 'POST':
        nombreliga = request.POST.get('nombreliga')
        nombretorneo = request.POST.get('nombretorneo')
        año = request.POST.get('año')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        reglamento = request.FILES.get('reglamento')  # <-- Aquí debe usarse paréntesis

        temporada = Temporada.objects.get(pk=id)
        temporada.nombreliga = nombreliga
        temporada.nombretorneo = nombretorneo
        temporada.año = año
        temporada.fecha_inicio = fecha_inicio
        temporada.fecha_fin = fecha_fin

        # Solo actualizamos el reglamento si se subió un archivo nuevo
        if reglamento:
            temporada.reglamento = reglamento

        temporada.save()
        messages.success(request, "Temporada actualizada correctamente")
        return redirect('/temporadas')
    else:
        return redirect('/temporadas')


def eliminarTemporada(request, id):
    temporada = get_object_or_404(Temporada, pk=id)
    temporada.delete()
    messages.success(request, "Temporada eliminada correctamente")
    return redirect('temporadas')