#2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
#algoritmos necesarios para resolver las siguientes tareas:
#a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
#cantidad de episodios en los que aparecieron juntos ambos personajes que se
#relacionan;
#d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda,
#Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

from grafo import Grafo

grafo = Grafo (dirigido=False)

grafo.insert_vertice('Luke Skywalker')
grafo.insert_vertice('Darth Vader')
grafo.insert_vertice('Yoda')
grafo.insert_vertice('Boba Fett')
grafo.insert_vertice('C3PO')
grafo.insert_vertice('Leia')
grafo.insert_vertice('Rey')
grafo.insert_vertice('Kylo Ren')
grafo.insert_vertice('Chewbacca')
grafo.insert_vertice('Han Solo')
grafo.insert_vertice('R2D2')
grafo.insert_vertice('BB8')

grafo.insert_arist('Luke Skywalker', 'Leia', 4)
grafo.insert_arist('Darth Vader', 'Yoda', 2)
grafo.insert_arist('Yoda', 'Boba Fett', 1)
grafo.insert_arist('C3PO', 'Leia', 3)
grafo.insert_arist('Rey', 'Kylo Ren', 2)
grafo.insert_arist('Chewbacca', 'Han Solo', 4)
grafo.insert_arist('R2D2', 'BB8', 1)

#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;

print('Arbol de expanción minima')
bosque= grafo.kruskal()

cont=0
for arbol in bosque:
    for nodo in arbol.split(';'):
        partes = nodo.split('-')
        print(partes)
        if ('Yoda') in partes:
            cont+=1

if cont>=1:
    print('Yoda está')

#c) determinar cuál es el número máximo de episodio que comparten dos personajes,
#y quienes son.
expancionMinima= grafo.kruskal()

max_value = 0
max_node = []
for tree in expancionMinima:
    for node in tree.split(";"):
        value = node.split("-")
        print(node)
        valor=value[-1]
        if int(valor) > max_value:
            max_value = int(valor)
            max_node = value

print(f"Arista de valor maximo: {max_node[0]} y {max_node[1]} comparten {max_value} episodios")
