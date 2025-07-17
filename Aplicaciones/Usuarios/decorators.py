from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from functools import wraps

def rol_requerido(rol_permitido):
    def decorator(view_func):
        @wraps(view_func)
        @login_required(login_url='/')
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'perfilusuario') and request.user.perfilusuario.rol == rol_permitido:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator
