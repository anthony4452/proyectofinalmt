from django import template

register = template.Library()

@register.filter
def get_jugador_carnet(carnets, jugador_id):
    for c in carnets:
        if c.jugador.id == jugador_id:
            return True
    return False
