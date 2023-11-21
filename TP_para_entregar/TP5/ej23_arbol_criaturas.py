#23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
#resuelva las siguientes consultas:

#b. se debe permitir cargar una breve descripción sobre cada criatura;
#c. mostrar toda la información de la criatura Talos;

#e. listar las criaturas derrotadas por Heracles;
#f. listar las criaturas que no han sido derrotadas;

#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;

#j. eliminar al Basilisco y a las Sirenas;
#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#derroto a varias;
#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
#m. realizar un listado por nivel del árbol;
#n. muestre las criaturas capturadas por Heracles.

from arbol_binario import BinaryTree


arbol = BinaryTree()

datos = [
    {'name': 'Medusa', 'derrotado': 'Perseo'},
    {'name': 'Medusa2', 'derrotado': 'Zeus'},
    {'name': 'Tifon', 'derrotado': 'Zeus'},
    {'name': 'Leon Nimea', 'derrotado': 'Heracles'},
    {'name': 'Hydrade lerna', 'derrotado': 'Heracles'},
    {'name': 'Otro', 'derrotado': 'Heracles'},
    {'name': 'Ceto', 'derrotado': None},
    {'name': 'Tore de Creta', 'derrotado': None},
    {'name': 'Ceto2', 'derrotado': "Apolo"},
    {'name': 'Ceto3', 'derrotado': "Apolo"},

]

for criatura in datos:
    arbol.insert_node(criatura['name'], {'derrotado': criatura['derrotado']})

#a. listado inorden de las criaturas y quienes la derrotaron;
print ('a. listado inorden de las criaturas y quienes la derrotaron')
arbol.inorden()
print()

#b. se debe permitir cargar una breve descripción sobre cada criatura;
print('b. se debe permitir cargar una breve descripción sobre cada criatura;')
arbol.inorden_add_field_criaturas('Descripcion',None)
arbol.inorden()
print()

#c. mostrar toda la información de la criatura Talos;
print('c. mostrar toda la información de la criatura Talos;')
bus = arbol.search('Talos')

if bus is not None:
    print ('La información de Talos es: ', bus.value, bus.other_values)
else:
    print ('Talos no se encuentra en el arbol.')
print()

#d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas; 
print('d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas; ')
dic_ranking = {}
arbol.inorden_ranking(dic_ranking)

def order_por(item):
    return item[1]

ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print(ordenados[:3])

#e. listar las criaturas derrotadas por Heracles;
print('e. listar las criaturas derrotadas por Heracles;')
arbol.inorden_derrotas('Heracles')
print()

#f. listar las criaturas que no han sido derrotadas;
print('f. listar las criaturas que no han sido derrotadas;')
arbol.inorden_derrotas(None)
print()

#g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
print('g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;')
arbol.inorden_add_field_criaturas('Capturado',None)
arbol.inorden()
print()

#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;
print('h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;')
buscados=['Cerbero','Toro de Creta','Cierva de Cerinea','Jabali de Erimanto']

arbol.inorden_modify_fields(buscados,'Capturado','Heracles')
arbol.inorden()
print()

#i. se debe permitir búsquedas por coincidencia;
print ('i. se debe permitir búsquedas por coincidencia;')
buscado=input('Ingrese criatura que busca: ')
arbol.search_by_coincidence(buscado)

#j. eliminar al Basilisco y a las Sirenas;
print ('j. eliminar al Basilisco y a las Sirenas;')
buscado=arbol.search('Basilisco')
if buscado is not None:
    arbol.delete_node('Basilisco')
    print('Se elimino al basilisco')

buscado=arbol.search('Sirenas')
if buscado is not None:
    arbol.delete_node('Sirenas')
    print('Se elimino a las sirenas')

arbol.inorden()
print()

#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#derroto a varias;
print('k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;')
arbol.inorden_modify_fields('Aves del Estínfalo','Derrotado','Heracles')
arbol.inorden()
print()

#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
print('l. modifique el nombre de la criatura Ladón por Dragón Ladón;')
buscado=arbol.search('Ladón')
if buscado is not None:
    otherValuesBuscado= buscado.other_values
    arbol.delete_node('Ladón')
    arbol.insert_node('Dragón Ladón',otherValuesBuscado)

arbol.inorden()
print()

#m. realizar un listado por nivel del árbol;
print('m. realizar un listado por nivel del árbol;')
arbol.by_level()
print()

#n. muestre las criaturas capturadas por Heracles.
print('n. muestre las criaturas capturadas por Heracles.')
arbol.inorden_capture('Heracles')
print()





