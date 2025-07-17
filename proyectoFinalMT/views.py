from django.shortcuts import render

def error_403_view(request, exception):
    return render(request, '403.html', status=403)


def prueba_error_404(request):
    return render(request, '404.html', status=404)
