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
grafo.insert_vertice('C-3PO')
grafo.insert_vertice('Leia')
grafo.insert_vertice('Rey')
grafo.insert_vertice('Kylo Ren')
grafo.insert_vertice('Chewbacca')
grafo.insert_vertice('Han Solo')
grafo.insert_vertice('R2D2')
grafo.insert_vertice('BB-8')

grafo.insert_arist('Luke Skywalker', 'Leia', 4)
grafo.insert_arist('Darth Vader', 'Yoda', 2)
grafo.insert_arist('Yoda', 'Boba Fett', 1)
grafo.insert_arist('C-3PO', 'Leia', 3)
grafo.insert_arist('Rey', 'Kylo Ren', 2)
grafo.insert_arist('Chewbacca', 'Han Solo', 4)
grafo.insert_arist('R2-D2', 'BB-8', 1)
