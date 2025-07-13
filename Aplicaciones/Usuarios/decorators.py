from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def rol_requerido(rol_permitido):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if hasattr(request.user, 'perfilusuario') and request.user.perfilusuario.rol == rol_permitido:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied  # Retorna error 403
        return _wrapped_view
    return decorator
