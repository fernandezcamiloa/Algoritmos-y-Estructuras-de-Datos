# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias
# para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.


from lista import Lista
#from random import randint


class Superheroe ():

    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        return f'{self.nombre} - {self.anio_aparicion} - {self.casa_comic} - {self.biografia}'

s1 = Superheroe('Linterna verde', 1970, 'DC', 'Horrible peli')
s2 = Superheroe('Hulk', 1962, 'Marvel', 'No usa armadura')
s3 = Superheroe('Dr. Strange', 1963, 'DC', 'un capo')

Superheroes = [s1, s2, s3]

lista_superheroes = Lista()

#for Superheroe in Superheroes 
#lista_superheroes.delete('Linterna Verde','nombre')
#lista_superheroes.barrido()
print(Superheroe)
