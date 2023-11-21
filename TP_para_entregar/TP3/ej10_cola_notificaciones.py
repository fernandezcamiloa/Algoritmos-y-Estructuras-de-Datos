# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, sin perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

from cola import Cola
from pila import Pila


class Notificacion ():
    def __init__(self, hora, app, mensaje):
        self.__hora = hora
        self.__app = app
        self.__mensaje = mensaje

    def get_hora(self):
        return self.__hora

    def get_app(self):
        return self.__app

    def get_mensaje(self):
        return self.__mensaje

    def __str__(self):
        return (f"{self.__hora}, {self.__app}, {self.__mensaje}")

cola_aux = Cola ()
cola_notificaciones = Cola ()
notificaciones = [
    Notificacion('8:50', 'Facebook', 'Bienvenido'),
    Notificacion('11:30', 'Twitter', 'Aprenda Python'),
    Notificacion('12:30', 'Twitter', 'Gran escandalo'),
    Notificacion('13:30', 'Facebook', 'Feliz cumple'),
    Notificacion('14:00', 'Twitter', '10 cosas que no sabias de Python'),
    Notificacion('16:00', 'Instagram', 'Juan agrego una foto')
]

for notif in notificaciones:
    cola_notificaciones.arrive(notif)
#    print (cola_notificaciones.size())
#    print (notif.get_hora(), notif.get_app(), notif.get_mensaje())
    

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
print ('a. escribir una función que elimine de la cola todas las notificaciones de Facebook;')
def eliminar_notificaciones_facebook(cola):
    nueva_cola = Cola()
    while cola.size() > 0:
        notificacion = cola.atention()
        if notificacion.get_app() != 'Facebook':
            nueva_cola.arrive(notificacion)
    return nueva_cola
    

cola_notificaciones = eliminar_notificaciones_facebook(cola_notificaciones)


print ()
#b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, sin perder datos en la cola;
print ('b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, sin perder datos en la cola;')
def mostrar_notificaciones_twitter_con_python(cola):
    cola_temporal = Cola()
    while cola.size() > 0:
        notificacion = cola.atention()
        if notificacion.get_app() == 'Twitter' and 'Python' in notificacion.get_mensaje():
            print(notificacion)
        cola_temporal.arrive(notificacion)
    while cola_temporal.size() > 0:
        cola.arrive(cola_temporal.atention())

mostrar_notificaciones_twitter_con_python(cola_notificaciones)

print ()
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.
print('c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.')
def notificaciones_entre_horas(cola, pila, hora_inicio, hora_fin):
    while cola.size() > 0:
        notificacion = cola.atention()
        if hora_inicio <= notificacion.get_hora() <= hora_fin:
            pila.push(notificacion)

    print("Número de notificaciones entre", hora_inicio, "y", hora_fin, ":", pila.size())

    while pila.size() > 0:
        cola.arrive(pila.pop())

pila_temporal = Pila()
notificaciones_entre_horas(cola_notificaciones, pila_temporal, '11:43', '15:57')



