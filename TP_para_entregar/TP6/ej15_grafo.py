#15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
#y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
#a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
#uno en las naturales) y tipo (natural o arquitectónica);
#b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
#la distancia que las separa;
#c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
#d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
#e. determinar si algún país tiene más de una maravilla del mismo tipo;
#f. deberá utilizar un grafo no dirigido.

from grafo import Grafo

grafo = Grafo(dirigido=False)

class Maravilla:
    
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.nombre}-{self.pais}-{self.tipo}'


   
grafo.insert_vertice(Maravilla("Gran Muralla", ['China'], 'Arquitectonica'), criterio='nombre')
grafo.insert_vertice(Maravilla("Coliseo Romano", ['Peru'], 'Arquitectonica'), criterio='nombre')
grafo.insert_vertice(Maravilla("Torre Eiffel", ['Francia'], 'Arquitectonica'), criterio='nombre')
grafo.insert_vertice(Maravilla("Cataratas de Iguazu", ['Argentina', 'Brasil'], 'Natural'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Isla Jeju", ['Corea del Sur'], 'Natural'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Montaña de la Mesa", ['Sudafrica'], 'Natural'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Cristo Redentor", ['Brasil'], 'Arquitectonica'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Piramides de Giza", ['Egypto'], 'Arquitectonica'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Opera de Sydney", ['Australia'], 'Arquitectonica'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Parque Nacional de Komodo", ['Indonesia'], 'Natural'), criterio= 'nombre')
grafo.insert_vertice(Maravilla("Río subterráneo de Puerto Princesa", ['Filipinas'], 'Natural'), criterio= 'nombre')


grafo.insert_arist('Gran Muralla', 'Coliseo Romano', 8, criterio_vertice='nombre')
grafo.insert_arist('Coliseo Romano', 'Torre Eiffel', 12, criterio_vertice='nombre')
grafo.insert_arist('Cataratas de Iguazu', 'Isla Jeju', 76, criterio_vertice='nombre')
grafo.insert_arist('Isla Jeju', 'Montaña de la Mesa', 66, criterio_vertice='nombre')
grafo.insert_arist('Montaña de la Mesa', 'Parque Nacional de Komodo', 86, criterio_vertice='nombre')
grafo.insert_arist('Parque Nacional de Komodo', 'Río subterráneo de Puerto Princesa', 35, criterio_vertice='nombre')
grafo.insert_arist('Cristo Redentor', 'Piramides de Giza', 123, criterio_vertice='nombre')
grafo.insert_arist('Piramides de Giza', 'Torre Eiffel', 45, criterio_vertice='nombre')
grafo.insert_arist('Piramides de Giza', 'Opera de Sydney', 45, criterio_vertice='nombre')


print('BARRIDO: ')
grafo.barrido()
print()

#!B
print('CAMINO MÁS CORTO')
ori = 'Gran Muralla'
des = 'Torre Eiffel'
origen = grafo.search_vertice(ori, criterio='nombre')
destino = grafo.search_vertice(des, criterio='nombre')
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(grafo.has_path(ori, des, criterio='nombre')):
        camino_mas_corto = grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value[2]
print()

#!C.1
print('ARBOL DE EXPANSIÓN MÍNIMA -- ARQUITECTURAS')
print()
grafo_A = Grafo(dirigido=False)

grafo_A.insert_vertice(Maravilla("Gran Muralla", ['China'], 'Arquitectonica'), criterio='nombre')
grafo_A.insert_vertice(Maravilla("Coliseo Romano", ['Peru'], 'Arquitectonica'), criterio='nombre')
grafo_A.insert_vertice(Maravilla("Torre Eiffel", ['Francia'], 'Arquitectonica'), criterio='nombre')
grafo_A.insert_vertice(Maravilla("Cristo Redentor", ['Brasil'], 'Arquitectonica'), criterio= 'nombre')
grafo_A.insert_vertice(Maravilla("Piramides de Giza", ['Egypto'], 'Arquitectonica'), criterio= 'nombre')
grafo_A.insert_vertice(Maravilla("Opera de Sydney", ['Australia'], 'Arquitectonica'), criterio= 'nombre')

grafo_A.insert_arist('Gran Muralla', 'Coliseo Romano', 8, criterio_vertice='nombre')
grafo_A.insert_arist('Coliseo Romano', 'Torre Eiffel', 12, criterio_vertice='nombre')
grafo_A.insert_arist('Cristo Redentor', 'Piramides de Giza', 123, criterio_vertice='nombre')
grafo_A.insert_arist('Piramides de Giza', 'Torre Eiffel', 45, criterio_vertice='nombre')
grafo_A.insert_arist('Piramides de Giza', 'Opera de Sydney', 45, criterio_vertice='nombre')

bosque_A = grafo_A.kruskal()
for arbol in bosque_A:
    for nodo in arbol.split(';'):
        print(nodo)
print()

#!C.2
print('ARBOL DE EXPANSIÓN MÍNIMA -- NATURALES')
print()
grafo_N = Grafo(dirigido=False)

grafo_N.insert_vertice(Maravilla("Cataratas de Iguazu", ['Argentina', 'Brasil'], 'Natural'), criterio= 'nombre')
grafo_N.insert_vertice(Maravilla("Isla Jeju", ['Corea del Sur'], 'Natural'), criterio= 'nombre')
grafo_N.insert_vertice(Maravilla("Montaña de la Mesa", ['Sudafrica'], 'Natural'), criterio= 'nombre')
grafo_N.insert_vertice(Maravilla("Parque Nacional de Komodo", ['Indonesia'], 'Natural'), criterio= 'nombre')
grafo_N.insert_vertice(Maravilla("Río subterráneo de Puerto Princesa", ['Filipinas'], 'Natural'), criterio= 'nombre')

grafo_N.insert_arist('Cataratas de Iguazu', 'Isla Jeju', 76, criterio_vertice='nombre')
grafo_N.insert_arist('Isla Jeju', 'Montaña de la Mesa', 66, criterio_vertice='nombre')
grafo_N.insert_arist('Montaña de la Mesa', 'Parque Nacional de Komodo', 86, criterio_vertice='nombre')
grafo_N.insert_arist('Parque Nacional de Komodo', 'Río subterráneo de Puerto Princesa', 35, criterio_vertice='nombre')

bosque_N = grafo_N.kruskal()
for arbol in bosque_N:
    for nodo in arbol.split(';'):
        print(nodo)
print()


#d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
print ('d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;')
pais=input('Ingrese pais para ver si dispone de maravillas arquitectónicas y naturales: ')
print(grafo.barrido_maravillas(pais))
print()

#e. determinar si algún país tiene más de una maravilla del mismo tipo;
print ('e. determinar si algún país tiene más de una maravilla del mismo tipo;')
pais2=input('Ingrese pais para ver si dispone más de una maravilla del mismo tipo: ')
print(grafo.barrido_tipos(pais2))
#f. deberá utilizar un grafo no dirigido.