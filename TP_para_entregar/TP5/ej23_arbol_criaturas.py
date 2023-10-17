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
#a. listado inorden de las criaturas y quienes la derrotaron;
for criatura in datos:
    arbol.insert_node(criatura['name'], {'derrotado': criatura['derrotado']})

print ('a. listado inorden de las criaturas y quienes la derrotaron')



#g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
#o dios que la capturo;
print ('g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;')
arbol.inorden_add_field()

#d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print ('d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;')
dic_ranking = {}
arbol.inorden_ranking(dic_ranking)

print(dic_ranking)


def order_por(item):
    print(item)
    return item[1]

ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print(ordenados[:3])

#no se cual es este
print ('no c cual es')
pos = arbol.search('')
if pos is not None:
    pos.other_values['capturado'] = 'Heracles'

#i. se debe permitir búsquedas por coincidencia;
print ('i. se debe permitir búsquedas por coincidencia;')
arbol.search_by_coincidence('')