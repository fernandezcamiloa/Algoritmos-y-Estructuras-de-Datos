# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
# de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
# la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# ok a. obtener la cantidad de Pokémons de un determinado entrenador;
# ok b. listar los entrenadores que hayan ganado más de tres torneos;
# ok c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# ok e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
# o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

from lista_lista import Lista
from random import randint


class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbp{self.cb_perdidas}-cbg{self.cb_ganadas}'


class Pokemon():

    def __init__(self, nombre, nivel=1, tipo=None, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', 7, 80, 90)
e2 = Entrenador('Maria', 10, 20, 120)
e3 = Entrenador('Ana', 40, 12, 20)

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()


p1 = Pokemon('Pikachu', 100, 'electrico')
p2 = Pokemon('Jolteon', 50,  'electrico')
p3 = Pokemon('Vaporeon', 46, 'agua', 'hielo')
p4 = Pokemon('Flareon', 12,  'fuego')
p5 = Pokemon('Zapdos', 62, 'electrico', 'volador')
p6 = Pokemon('Pelipper', 81, 'agua', 'volador')

pokemons = [p1, p2, p3, p4, p5, p6]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


#! a. obtener la cantidad de Pokémons de un determinado entrenador;
print ('a. obtener la cantidad de Pokémons de un determinado entrenador')
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
#! b. listar los entrenadores que hayan ganado más de tres torneos;
print ('b. listar los entrenadores que hayan ganado más de tres torneos')
lista_entrenadores.barrido_cantidad_torneos_ganados(3)
print()

#! c el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print ('c el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados')
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

pokemon_mayor = sublista.get_element_by_index(0)
for pos in range(1, sublista.size()):
    pokemon = sublista.get_element_by_index(pos)
    if pokemon.nivel > pokemon_mayor.nivel:
        pokemon_mayor = pokemon

print(
    f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')


# d. mostrar todos los datos de un entrenador y sus Pokémos;
print ('d. mostrar todos los datos de un entrenador y sus Pokémos;')
lista_entrenadores.barrido_entrenadores()
print()

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print ('e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %')
lista_entrenadores.barrido_porcentaje_batallas_79()
print()

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print ('f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)')

for i in range(lista_entrenadores.size()):
    elem=lista_entrenadores.get_element_by_index(i)
    entrenador,pokemones=elem[0],elem[1]
    for j in range (pokemones.size()):
        if (pokemones.get_element_by_index(j).tipo=='fuego' and pokemones.get_element_by_index(j).subtipo=='planta') or (pokemones.get_element_by_index(j).tipo=='agua' and pokemones.get_element_by_index(j).subtipo=='volador'):
            print(f'{entrenador.nombre} tiene pokenon de tipo fuego/planta o agua/volador')

print()
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print ('g. el promedio de nivel de los Pokémons de un determinado entrenador;')
entrenador = 'Juan'
buscado=lista_entrenadores.search(entrenador,'nombre')
promedio=0
if buscado != None:
    value=lista_entrenadores.get_element_by_index(buscado)
    pokemones=value[1]
    acum=0
    for i in range(pokemones.size()):
        nivel=pokemones.get_element_by_index(i).nivel
        acum+=nivel
        promedio=acum//(pokemones.size())
print(f'el promedio de nivel de los Pokemones de {entrenador} es {promedio} .')

print()
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print ('h. determinar cuántos entrenadores tienen a un determinado Pokémon;')
contador = 0
pokemon = 'Jolteon'
for pos in range(lista_entrenadores.size()):
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    for pos in range(sublista.size()):
        value = sublista.get_element_by_index(pos)
        if value.nombre == pokemon:
            contador += 1
            break
print(f'{contador} entrenadores tienen a {pokemon}.')

print()
# i. mostrar los entrenadores que tienen Pokémons repetidos;
print ('i. mostrar los entrenadores que tienen Pokémons repetidos;')
for pos in range(lista_entrenadores.size()):
    value = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = value[0], value[1]
    contador = 0
    for x in range(sublista.size()-1):
        pri = sublista.get_element_by_index(x)
        siguiente = sublista.get_element_by_index(x+1)
        if pri.nombre == siguiente.nombre:
            contador += 1
            break
    if contador == 1:
        print(f'El entrenador {entrenador.nombre} tiene pokemons repetidos.')
        
#    else:
#        print(f'El entrenador {entrenador.nombre} no tiene pokemons repetidos.')
#        print('--------')

print()
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
# o Wingull;
print ('j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;')


for i in range(lista_entrenadores.size()):
    valor = lista_entrenadores.get_element_by_index(i)
    entrenador, sublista = valor[0], valor[1]
    cont = 0
    for i in range(sublista.size()):
        pokemon = sublista.get_element_by_index(i)
        if pokemon.nombre == 'Tyrantrum'or 'Terrakion'or 'Wingull':
            print(f'{entrenador.nombre} tiene a Willgull o Terrakion o Tyrantrum en su equipo.')
            cont += 1
    if cont == 0:
        print(f'El entrenador {entrenador.nombre} no tiene a Willgull o Terrakion o Tyrantrum en su equipo.')
    else: 
        pass
print()

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
print ('k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados')
#entren=input('Ingrese Entrenador: ')
#buscadox= lista_entrenadores.search(entren, 'nombre')
buscadox= lista_entrenadores.search('Juan', 'nombre')

if buscadox != None:
    elem2=lista_entrenadores.get_element_by_index(buscadox)
    sublista=elem2[1]
#    pokemon=input('Ingrese pokemon a consultar: ')
    buscadoy=sublista.search('Picachu','nombre')
    if buscadoy !=None:
        print(f'El entrenador{buscadox} tiene a {pokemon}')
    else:
        print(f'El entrenador {buscadox} no tiene a {pokemon}')
else:
    print('El entrenador no esta')
