from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .decorators import rol_requerido  # Donde guardes el decorador
from django.db import transaction
from .models import PerfilUsuario
from django.contrib.auth.models import User
from Aplicaciones.Temporadas.models import Temporada

from django.utils import timezone

def get_temporada_activa():
    hoy = timezone.now().date()
    return Temporada.objects.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy).first()


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


def error_403_view(request, exception):
    rol = None
    if request.user.is_authenticated:
        try:
            rol = request.user.perfilusuario.rol
        except PerfilUsuario.DoesNotExist:
            rol = None
    return render(request, '403.html', {'rol': rol}, status=403)

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
            return redirect('login')
        except Exception as e:
            return render(request, 'registro.html', {'error': f'Error al registrar: {str(e)}'})

    return render(request, 'registro.html')



@rol_requerido('admin')
def admin_dashboard(request):
    rol = request.user.perfilusuario.rol
    
    temporada = get_temporada_activa()
    
    return render(request, 'admin_dashboard.html', {
        'rol': rol,
        'temporada_id': temporada.id if temporada else None,
    })
@rol_requerido('vocal')
def vocal_dashboard(request):
    rol = request.user.perfilusuario.rol
    temporada = get_temporada_activa()


    return render(request, 'vocal_dashboard.html', {
            'rol': rol,
            'temporada_id': temporada.id if temporada else None,
        })