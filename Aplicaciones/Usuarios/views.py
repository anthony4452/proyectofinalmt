from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PerfilUsuario
from django.db import IntegrityError
from django.db import transaction

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            try:
                perfil = PerfilUsuario.objects.get(usuario=usuario)
                if perfil.rol == 'admin':
                    return redirect('admin_dashboard')
                elif perfil.rol == 'vocal':
                    return redirect('vocal_dashboard')
            except PerfilUsuario.DoesNotExist:
                logout(request)
                return render(request, 'login.html', {'error': 'Perfil de usuario no encontrado'})
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        rol = request.POST.get('rol')

        if not username or not email or not password1 or not password2 or not rol:
            return render(request, 'registro.html', {'error': 'Todos los campos son obligatorios'})

        if password1 != password2:
            return render(request, 'registro.html', {'error': 'Las contraseñas no coinciden'})

        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'El usuario ya existe'})

        try:
            with transaction.atomic():
                user = User.objects.create_user(username=username, email=email, password=password1)
                PerfilUsuario.objects.create(usuario=user, rol=rol)
            return redirect('login')  # Asegúrate que esta vista exista
        except Exception as e:
            return render(request, 'registro.html', {'error': f'Error al registrar: {str(e)}'})

    return render(request, 'registro.html')

@login_required
def admin_dashboard(request):
    rol = request.user.perfilusuario.rol
    return render(request, 'admin_dashboard.html', {'rol': rol})

@login_required
def vocal_dashboard(request):
    rol = request.user.perfilusuario.rol
    return render(request, 'vocal_dashboard.html', {'rol': rol})

