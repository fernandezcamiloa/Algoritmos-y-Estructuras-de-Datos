#1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
#de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
#tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:

from arbol_binario import BinaryTree

lista_pokemones = [
    {'name': 'Pikachu', 'number': 25, 'tipo': 'electrico' },
    {'name': 'Vaporeon', 'number': 125, 'tipo': 'agua/hielo' },
    {'name': 'Jolteon', 'number': 126, 'tipo': 'electrico' },
    {'name': 'Lycanroc', 'number': 326, 'tipo': 'roca' },
    {'name': 'Tyrantrum', 'number': 426, 'tipo': 'roca/dragon' },
    {'name': 'Steelix', 'number': 226, 'tipo': 'acero' },
    {'name': 'Cindaquil', 'number': 168, 'tipo': 'fuego' },
    {'name': 'Bellsprout', 'number': 48, 'tipo': 'planta' },
]

#a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()


for pokemon in lista_pokemones:
    arbol_nombre.insert_node(pokemon['name'], {"number": pokemon['number'], "tipo": pokemon ['tipo']})
    arbol_numero.insert_node (pokemon ['number'], {'name': pokemon['name'], "tipo": pokemon ['tipo']})
    arbol_tipo.insert_node (pokemon ['tipo'], {'name': pokemon['name'],"number": pokemon['number']})


#b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
#caracteres–;
print ('b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, ...')
arbol_numero.inorden_number(25)
arbol_nombre.search_by_coincidence_pokemon('Jol')

#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua,
#fuego, planta y eléctrico;
print ('c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua,fuego, planta y eléctrico')
arbol_tipo.search_by_coincidence_pokemon('fuego')
arbol_tipo.search_by_coincidence_pokemon('planta')
arbol_tipo.search_by_coincidence_pokemon('electrico')

#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#además un listado por nivel por nombre;
print('d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;')
print ('por nombre: ')
arbol_nombre.inorden_pokemon()
print ('por numero: ')
arbol_numero.inorden_pokemon()
print ('by level: ')
arbol_nombre.by_level()

#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
print ('e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;')
arbol_nombre.search_by_coincidence_pokemon('Jolteon')
arbol_nombre.search_by_coincidence_pokemon('Lycanroc')
arbol_nombre.search_by_coincidence_pokemon('Tyrantrum')

#f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
print ('f) Determina cuantos Pokémons hay de tipo eléctrico y acero.')
print('cantidad de electricos', arbol_tipo.contar_tipo('electrico'))
print('cantidad de acero', arbol_tipo.contar_tipo('acero'))
