
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


def usuarios_list(request):
    usuarios = User.objects.all()
    return render(request, "users.html", {'usuarios': usuarios})


def usuarios_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente")
            return redirect('usuarios_list')
    else:
        form = UserCreationForm()
    return render(request, "form.html", {'form': form})


def usuarios_edit(request, id):
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado exitosamente")
            return redirect('usuarios_list')
    else:
        form = UserChangeForm(instance=usuario)
    return render(request, "form.html", {'form': form})


def usuarios_delete(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, "Usuario eliminado exitosamente")
    return redirect('usuarios_list')
