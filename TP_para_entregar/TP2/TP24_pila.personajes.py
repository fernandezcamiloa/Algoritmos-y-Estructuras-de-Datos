# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:


from pila import Pila
from pila import PersonajeMCU


pilaPersonajes = Pila()
personajes = [
    PersonajeMCU("Groot",  7),
    PersonajeMCU("Thor",  5),
    PersonajeMCU("Rocket Raccoon",  8),
    PersonajeMCU("Iron Man", 3),
    PersonajeMCU("Black Widow",  2),
    PersonajeMCU("Capitan America",  9),
    PersonajeMCU("Daredevill",  2)
]

for personaje in personajes:
    pilaPersonajes.push(personaje)

posicion = 1

while pilaPersonajes.size() > 0:
    personaje = pilaPersonajes.pop()
    if (not personaje):
        continue
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
    if (personaje.get_name() == 'Rocket Raccoon' or personaje.get_name() == 'Groot'):
        print(f'{personaje.get_name()}, posicion {posicion}')
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
    if (personaje.get_movie_amount() > 5):
        print(
            f'El personaje {personaje.get_name()} participo en mas de 5 peliculas, participo en {personaje.get_movie_amount()}')
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
    if (personaje.get_name() == 'Black Widow'):
        print(
            f'El personaje Black Widow aparecio en {personaje.get_movie_amount()} peliculas')
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
    if (personaje.get_name()[0] == 'C' or personaje.get_name()[0] == 'D' or personaje.get_name()[0] == 'G'):
        print(
            f'El personaje {personaje.get_name()} empieza con {personaje.get_name()[0]}')

    posicion = posicion + 1
