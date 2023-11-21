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
s4 = Superheroe('Wolverine', 1973, 'Marvel', 'guepardo')
s5 = Superheroe('Capitana Marvel', 1960, 'Marvel', 'señora marvel')
s6 = Superheroe('Mujer Maravilla', 1958, 'DC', 'señora amazona')
s7 = Superheroe('Flash', 1970, 'DC', 'usa traje rojo')
s8 = Superheroe('Star Lord', 1977, 'Marvel', 'el Chris')

superheroes = [s1, s2, s3, s4, s5, s6, s7, s8]

lista_superheroes = Lista()

for Superheroe in superheroes:
    lista_superheroes.insert(Superheroe, 'nombre')
#lista_superheroes.delete('Linterna Verde','nombre')
#lista_superheroes.barrido()
#print(get_element_by_index('nombre'))

# a. eliminar el nodo que contiene la información de Linterna Verde;
print ('a. eliminar el nodo que contiene la información de Linterna Verde;')
elemento=lista_superheroes.search('Linterna verde', 'nombre')
if  elemento != None:
    lista_superheroes.delete('Linterna verde','nombre')

print()
# b. mostrar el año de aparición de Wolverine;
print ('b. mostrar el año de aparición de Wolverine;')
elemento2=lista_superheroes.search('Wolverine', 'nombre')
if  elemento2 != None:
    print ('Anio: ',lista_superheroes.get_element_by_index(elemento2).anio_aparicion)
  
print()
# c. cambiar la casa de Dr. Strange a Marvel;
print ('c. cambiar la casa de Dr. Strange a Marvel;')
elemento3=lista_superheroes.search('Dr. Strange', 'nombre')
if elemento3 != None:
    lista_superheroes.get_element_by_index(elemento3).casa = 'Marvel'

print()
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
print ('d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;')
for i in range(0,lista_superheroes.size()):
   if  ('armadura' in lista_superheroes.get_element_by_index(i).biografia) or ('traje' in lista_superheroes.get_element_by_index(i).biografia):
       print ('Traje o Armadura: ', lista_superheroes.get_element_by_index(i).nombre)

print()
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
print ('e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;')
for i in range(lista_superheroes.size()):
    if lista_superheroes.get_element_by_index(i).anio_aparicion < 1963: 
        print('Año ', lista_superheroes.get_element_by_index(i).anio_aparicion, lista_superheroes.get_element_by_index(i).nombre,lista_superheroes.get_element_by_index(i).casa_comic)

print()
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print ('f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;')
elemento4=lista_superheroes.search('Capitana Marvel', 'nombre')
elemento5=lista_superheroes.search('Mujer Maravilla', 'nombre')
if elemento4!= None:
   print('Capitana Marvel:', lista_superheroes.get_element_by_index(elemento4).casa_comic) 
if elemento5!= None:
    print('Mujer Maravilla: ',lista_superheroes.get_element_by_index(elemento5).casa_comic) 

print()
# g. mostrar toda la información de Flash y Star-Lord;
print ('g. mostrar toda la información de Flash y Star Lord;')
elemento6=lista_superheroes.search('Flash', 'nombre')
elemento7=lista_superheroes.search('Star Lord', 'nombre')
if elemento6!= None:
   print(lista_superheroes.get_element_by_index(elemento6)) 
if elemento7!= None:
   print(lista_superheroes.get_element_by_index(elemento7)) 

print()
# h. listar los superhéroes que comienzan con la letra B, M y S;
print ('h. listar los superhéroes que comienzan con la letra B, M y S;')
for i in range(0, lista_superheroes.size()):
    if lista_superheroes.get_element_by_index(i).nombre[0] in ['B', 'M', 'S']:
        print(lista_superheroes.get_element_by_index(i)) 

print()
# i. determinar cuántos superhéroes hay de cada casa de comic.
print ('i. determinar cuántos superhéroes hay de cada casa de comic.')
contador_DC=0
contador_Marv=0

for i in range(0, lista_superheroes.size()):
    if lista_superheroes.get_element_by_index(i).casa_comic=='DC':
        contador_DC+=1
    else:
        contador_Marv +=1
print(f'hay {contador_DC} de DC  y {contador_Marv} de Marvel')
print()