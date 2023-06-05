# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.


class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje


def eliminar_notificaciones_facebook(cola):
    cola = [notif for notif in cola if notif.app != 'Facebook']
    return cola
    for notif in cola:
        print(f'{notif.hora} - {notif.app}: {notif.mensaje}')


def mostrar_notificaciones_twitter_python(cola):
    notificaciones_python = [
        notif for notif in cola if notif.app == 'Twitter' and 'Python' in notif.mensaje]
    for notif in notificaciones_python:
        print(f'{notif.hora} - {notif.app}: {notif.mensaje}')


def contar_notificaciones_pila(cola):
    pila_temporal = []
    contador = 0

    for notif in cola:
        if notif.hora >= '11:43' and notif.hora <= '15:57':
            pila_temporal.append(notif)

    while pila_temporal:
        notif = pila_temporal.pop()
        contador += 1

    return contador


cola_notificaciones = [
    Notificacion('8:50', 'Facebook', 'Bienvenido'),
    Notificacion('11:30', 'Twitter', 'Aprenda Python'),
    Notificacion('12:30', 'Twitter', 'Gran escandalo'),
    Notificacion('13:30', 'Facebook', 'Feliz cumple'),
    Notificacion('14:00', 'Twitter', '10 cosas que no sabias de Python'),
    Notificacion('16:00', 'Instagram', 'Juan agrego una foto')
]

cola_notificaciones = eliminar_notificaciones_facebook(cola_notificaciones)

mostrar_notificaciones_twitter_python(cola_notificaciones)

cantidad_notificaciones_pila = contar_notificaciones_pila(cola_notificaciones)
print(
    f'Son {cantidad_notificaciones_pila} las notificaciones entre 11:43 y 15:57 ')
