# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
# desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.


from random import randint


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


class PeliculaMarvel():

    def __init__(self, title, film_studio, year):
        self.__title = title
        self.__film_studio = film_studio
        self.__year = year

    def get_title(self):
        return self.__title

    def get_film_studio(self):
        return self.__film_studio    

    def get_year(self):
        return self.__year

    def __str__(self):
        return f'{self.__title} - {self.__film_studio} - {self.__year}'

pilaPeliculas = Pila()
pelis = [
PeliculaMarvel('Avengers End Game', 'Marvel Studios', 2018),
PeliculaMarvel('Thor Ragnarok', 'Marvel Studios', 2018),
PeliculaMarvel('Spiderman homecomming', 'Marvel Studios', 2014),
PeliculaMarvel('Iron Man',  'Marvel Studios', 2016),
PeliculaMarvel('Black Widow', 'Marvel Studios',  2016),
PeliculaMarvel('Shrek', 'Dreamworks', 2014),
PeliculaMarvel('Doctor Strange', 'Marvel Studios',  2016),
PeliculaMarvel('Hulk', 'Marvel Studios',  2018),
PeliculaMarvel('Red',  'Disney', 2022)
 ]


for peli in pelis:
    pilaPeliculas.push(peli)

contador_peliculas_de_2018 = 0

while pilaPeliculas.size() > 0:
    peli = pilaPeliculas.pop()
    if (not peli):
        continue
    if (peli.get_year() == 2014):
        print(f'La pelicula {peli.get_title()} se estreno en 2014')
    if (peli.get_year() == 2018):
        contador_peliculas_de_2018 = contador_peliculas_de_2018 + 1
    if (peli.get_year() == 2016 and peli.get_film_studio() == 'Marvel Studios'):
        print(f'Pelicula de Marvel Studios estrenada en 2016: {peli.get_title()}')
    

print(f'Se estrenaron {contador_peliculas_de_2018} peliculas en 2018')
