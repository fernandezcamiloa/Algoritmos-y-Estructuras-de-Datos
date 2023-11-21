

#5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
#(MCU), desarrollar un algoritmo que contemple lo siguiente:




from arbol_binario import BinaryTree

#a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': False},
    {'name': 'capitana Marvel', 'heroe': True},
    {'name': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])


#b. listar los villanos ordenados alfabéticamente;
print('Lista ordenada de villanos:')
arbol.inorden_super_or_villano(False)
print()

#c. mostrar todos los superhéroes que empiezan con C;
print('Superheroes que empiezan con C:')
arbol.inorden_start_with('C')

#d. determinar cuántos superhéroes hay el árbol;
print('cantidad de superheroes', arbol.contar_heroes())
print()

#f. listar los superhéroes ordenados de manera descendente;
print('Lista de superheroes ordenados de manera descendente:')
arbol.postorden_super_or_villano(True)
print()



#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#los villanos, luego resolver las siguiente tareas:
#I. determinar cuántos nodos tiene cada árbol;
arbol.division_arboles (arbol_heroes, arbol_villanos)
print('cantidad de nodos arbol heroes', arbol_heroes.contar_heroes())
print ('cantidad de nodos arbol villanos', arbol_villanos.contar_villanos())

#II. realizar un barrido ordenado alfabéticamente de cada árbol.
print ('barrido arbol heroes')
arbol_heroes.inorden()
print ('barrido arbol villanos')
arbol_villanos.inorden()

#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol
arbol.search_by_coincidence('do')

value = input('ingrese el nombre que desea modificar ')
pos = arbol.search(value)
if pos:
    is_hero = pos.other_values
    arbol.delete_node(value)
    print('modificar')
    new_value = input('ingrese en nuevo nombre ')
    arbol.insert_node(new_value, is_hero)
else:
    print('no se encontró')
print()
arbol.inorden()



arbol.by_level()