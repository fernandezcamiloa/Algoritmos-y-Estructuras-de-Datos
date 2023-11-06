#1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
#de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
#tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:




#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;


from arbol_binario import BinaryTree

lista_pokemones = [
    {'name': 'Pikachu', 'number': '25', 'tipo': 'electrico' },
    {'name': 'Vaporeon', 'number': '125', 'tipo': 'agua/hielo' },
    {'name': 'Jolteon', 'number': '126', 'tipo': 'electrico' },
    {'name': 'Lycanro', 'number': '326', 'tipo': 'roca' },
    {'name': 'Tyrantrum', 'number': '426', 'tipo': 'roca/dragon' },
    {'name': 'Steelix', 'number': '226', 'tipo': 'acero' },
]

#a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in lista_pokemones:
    arbol_nombre.insert_node (pokemon ['name'])
    arbol_numero.insert_node (pokemon ['number'])
    arbol_tipo.insert_node (pokemon ['tipo'])

#b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
#último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
#mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
#caracteres–;
arbol_nombre.search_by_coincidence('ste')
arbol_numero.inorden_start_with('25')


#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua,
#fuego, planta y eléctrico;
print ('c mostrar todos los nombres de todos los Pokémons de un determinado tipo agua,fuego, planta y eléctrico')
arbol_tipo.search_by_coincidence('Fuego')
arbol_tipo.search_by_coincidence('planta')
arbol_tipo.search_by_coincidence('electrico')


#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
#además un listado por nivel por nombre;
#b. listar los villanos ordenados alfabéticamente;
print('lista por nombre')
#arbol_nombre.inorden_nombre()
print()

#f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
print('cantidad de electricos', arbol_tipo.contar_electrico())
print ('cantidad de acero', arbol_tipo.contar_acero())

arbol.by_level()
