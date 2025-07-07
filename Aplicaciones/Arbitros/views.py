from django.shortcuts import render, redirect, get_object_or_404
from .models import Arbitro
from .forms import ArbitroForm
from django.contrib.auth.decorators import login_required, user_passes_test

# ✅ Verifica si el usuario es admin
def es_admin(user):
    return hasattr(user, 'perfilusuario') and user.perfilusuario.rol == 'admin'

@login_required
@user_passes_test(es_admin)
def arbitros(request):
    arbitros = Arbitro.objects.all()
    return render(request, 'arbitros.html', {'arbitros': arbitros})

@login_required
@user_passes_test(es_admin)
def nuevoArbitro(request):
    if request.method == 'POST':
        form = ArbitroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/arbitros/')
    else:
        form = ArbitroForm()
    return render(request, 'nuevoArbitro.html', {'form': form})

@login_required
@user_passes_test(es_admin)
def editarArbitro(request, id):
    arbitro = get_object_or_404(Arbitro, id=id)
    if request.method == 'POST':
        form = ArbitroForm(request.POST, instance=arbitro)
        if form.is_valid():
            form.save()
            return redirect('/arbitros/')
    else:
        form = ArbitroForm(instance=arbitro)
    return render(request, 'editarArbitro.html', {'form': form, 'arbitro': arbitro})

@login_required
@user_passes_test(es_admin)
def eliminarArbitro(request, id):
    arbitro = get_object_or_404(Arbitro, id=id)
    arbitro.delete()
    return redirect('/arbitros/')
