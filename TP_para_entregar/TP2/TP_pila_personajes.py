# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
# uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
# la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.


class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]


class PersonajeMCU():
    def __init__(self, name, movie_amount):
        self.__name = name
        self.__movie_amount = movie_amount

    def __str__(self):
        return f'Personaje: {self.__name}. Cantidad de peliculas: {self.__movie_amount}'

    def get_name(self):
        return self.__name

    def get_movie_amount(self):
        return self.__movie_amount


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
    if (personaje.get_name() == 'Rocket Raccoon' or personaje.get_name() == 'Groot'):
        print(f'{personaje.get_name()}, posicion {posicion}')

    if (personaje.get_movie_amount() > 5):
        print(
            f'El personaje {personaje.get_name()} participo en mas de 5 peliculas, participo en {personaje.get_movie_amount()}')

    if (personaje.get_name() == 'Black Widow'):
        print(
            f'El personaje Black Widow aparecio en {personaje.get_movie_amount()} peliculas')

    if (personaje.get_name()[0] == 'C' or personaje.get_name()[0] == 'D' or personaje.get_name()[0] == 'G'):
        print(
            f'El personaje {personaje.get_name()} empieza con {personaje.get_name()[0]}')

    posicion = posicion + 1

