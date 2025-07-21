from django.shortcuts import render, redirect, get_object_or_404
from .models import Correos
from Aplicaciones.Carnets.models import Carnet
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
import mimetypes


def correos_list(request):
    correos = Correos.objects.all()
    carnets = Carnet.objects.all()

    return render(request, 'correos.html', {'correos': correos, 'carnets': carnets})


def correos_form(request, id_editar=None):
    if request.method == 'POST':
        id_correo = request.POST.get('id_correo')
        if id_correo:
            correo = Correos.objects.get(id=id_correo)
        else:
            correo = Correos()

        correo.titulo = request.POST.get('titulo')
        correo.destinatario = request.POST.get('destinatario')
        correo.asunto = request.POST.get('asunto')
        correo.mensaje = request.POST.get('mensaje')

        carnet_id = request.POST.get('carnet')
        try:
            carnet = Carnet.objects.get(id=carnet_id)
            correo.carnet = carnet
        except Carnet.DoesNotExist:
            messages.error(request, "Carnet no válido")
            return redirect('correos_list')

        correo.save()

        if id_correo:
            messages.success(request, "Correo actualizado exitosamente")
        else:
            messages.success(request, "Correo guardado exitosamente")

        return redirect('correos_list')

    correos = Correos.objects.all()
    correo_editar = Correos.objects.get(id=id_editar) if id_editar else None
    carnet_selected = correo_editar.carnet.id if correo_editar else None
    carnets = Carnet.objects.all()
    return render(request, "correos.html", {
        'correos': correos,
        'correo_editar': correo_editar,
        'carnets': carnets,
        'carnet_selected': carnet_selected,
    })


def eliminar_correo(request, id):
    correo = get_object_or_404(Correos, id=id)
    correo.delete()
    messages.success(request, "Correo eliminado exitosamente")
    return redirect('correos_list')


def enviar_correo(request, id):
    correo = get_object_or_404(Correos, id=id)
    email = EmailMessage(
        subject=correo.asunto,
        body=correo.mensaje,
        from_email=settings.EMAIL_HOST_USER,
        to=[correo.destinatario],
    )

    if correo.carnet and correo.carnet.qr_code:
        qr_file = correo.carnet.qr_code
        file_type, _ = mimetypes.guess_type(qr_file.name)
        qr_file.open('rb')
        email.attach(qr_file.name, qr_file.read(), file_type)
        qr_file.close()

    email.send(fail_silently=False)
    messages.success(request, f"Correo enviado a {correo.destinatario}")
    return redirect('correos_list')
