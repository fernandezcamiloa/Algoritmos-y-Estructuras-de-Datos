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
from collections import Counter
from random import randint

def renglon():
    print("-------------------------")


mi_grafo = Grafo(dirigido=False)

class Maravilla:
    
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.nombre}-{self.pais}-{self.tipo}'



#VERTICES
mi_grafo.insert_vertice(Maravilla("Gran Muralla", 'China', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Machu Picchu", 'Peru', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Chichén Itza", 'México', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Ciudad de Petra", 'Jordania', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Taj Mahal", 'India', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Coliseo Romano", 'Italia', 'Arquitectonica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Cristo Redentor", 'Brasil', 'Arquitectonica'), criterio='nombre')

mi_grafo.insert_vertice(Maravilla("Cataras del Iguazú", 'Argentina', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Isla Jeju", 'Argentina', 'Sudafrica'), criterio='nombre')
mi_grafo.insert_vertice(Maravilla("Amazonia", 'Brasil', 'Natural'), criterio='nombre')


#ARISTAS Naturales
mi_grafo.insert_arist('Gran Muralla', 'Machu Picchu', 8, criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Sarasa', 8, criterio_vertice='nombre')


mi_grafo.insert_arist('Cataras del Iguazú', 'Isla Jeju', 7000, criterio_vertice='nombre')
mi_grafo.insert_arist('Cataras del Iguazú', 'Montaña de Mesa', 3090, criterio_vertice='nombre')
mi_grafo.insert_arist('Cataras del Iguazú', 'Amazonia', 400, criterio_vertice='nombre')
mi_grafo.insert_arist('Cataras del Iguazú', 'Bahía de Ha Long', 8000, criterio_vertice='nombre')
mi_grafo.insert_arist('Cataras del Iguazú', 'Parque Nacional de Komodo', 4000, criterio_vertice='nombre')
mi_grafo.insert_arist('Cataras del Iguazú', 'Río Subterráneo de Puerto Princesa', 12000, criterio_vertice='nombre')

mi_grafo.insert_arist('Isla Jeju', 'Montaña de Mesa', 6000,criterio_vertice='nombre')
mi_grafo.insert_arist('Isla Jeju', 'Amazonia',6600, criterio_vertice='nombre')
mi_grafo.insert_arist('Isla Jeju', 'Bahía de Ha Long', 3523, criterio_vertice='nombre')
mi_grafo.insert_arist('Isla Jeju', 'Parque Nacional de Komodo', 9552, criterio_vertice='nombre')
mi_grafo.insert_arist('Isla Jeju', 'Río Subterráneo de Puerto Princesa', 3299, criterio_vertice='nombre')

mi_grafo.insert_arist('Montaña de Mesa', 'Amazonia', 8765, criterio_vertice='nombre')
mi_grafo.insert_arist('Montaña de Mesa', 'Bahía de Ha Long', 2311, criterio_vertice='nombre')
mi_grafo.insert_arist('Montaña de Mesa', 'Parque Nacional de Komodo', 4342, criterio_vertice='nombre')
mi_grafo.insert_arist('Montaña de Mesa', 'Río Subterráneo de Puerto Princesa', 6543, criterio_vertice='nombre')

mi_grafo.insert_arist('Amazonia', 'Bahía de Ha Long', 3215, criterio_vertice='nombre')
mi_grafo.insert_arist('Amazonia', 'Parque Nacional de Komodo', 4324, criterio_vertice='nombre')
mi_grafo.insert_arist('Amazonia', 'Río Subterráneo de Puerto Princesa', 6546, criterio_vertice='nombre')

mi_grafo.insert_arist('Bahía de Ha Long', 'Parque Nacional de Komodo', 1232, criterio_vertice='nombre')
mi_grafo.insert_arist('Bahía de Ha Long', 'Río Subterráneo de Puerto Princesa', 4324, criterio_vertice='nombre')

mi_grafo.insert_arist('Parque Nacional de Komodo', 'Río Subterráneo de Puerto Princesa', 3231, criterio_vertice='nombre')


#ARISTAS Arq
mi_grafo.insert_arist('Ciudad de Petra', 'Taj Mahal', 1234, criterio_vertice='nombre')
mi_grafo.insert_arist('Ciudad de Petra', 'Machu Picchu', 4324, criterio_vertice='nombre')
mi_grafo.insert_arist('Ciudad de Petra', 'Chichén Itza', 5453, criterio_vertice='nombre')
mi_grafo.insert_arist('Ciudad de Petra', 'Coliseo Romano', 6465, criterio_vertice='nombre')
mi_grafo.insert_arist('Ciudad de Petra', 'Muralla China', 3442, criterio_vertice='nombre')
mi_grafo.insert_arist('Ciudad de Petra', 'Cristo Redentor', 2745, criterio_vertice='nombre')

mi_grafo.insert_arist('Taj Magal', 'Machu Picchu', 5362, criterio_vertice='nombre')
mi_grafo.insert_arist('Taj Magal', 'Chichén Itza', 2366, criterio_vertice='nombre')
mi_grafo.insert_arist('Taj Magal', 'Coliseo Romano', 6642, criterio_vertice='nombre')
mi_grafo.insert_arist('Taj Magal', 'Muralla China', 4422, criterio_vertice='nombre')
mi_grafo.insert_arist('Taj Magal', 'Cristo Redentor', 4343, criterio_vertice='nombre')

mi_grafo.insert_arist('Machu Picchu', 'Chichén Itza', 8767, criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Coliseo Romano', 6757, criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Muralla China', 9875, criterio_vertice='nombre')
mi_grafo.insert_arist('Machu Picchu', 'Cristo Redentor', 6546, criterio_vertice='nombre')

mi_grafo.insert_arist('Chichén Itza', 'Coliseo Romano', 4747, criterio_vertice='nombre')
mi_grafo.insert_arist('Chichén Itza', 'Muralla China', 9553, criterio_vertice='nombre')
mi_grafo.insert_arist('Chichén Itza', 'Cristo Redentor', 6547, criterio_vertice='nombre')

mi_grafo.insert_arist('Coliseo Romano', 'Muralla China', 6566, criterio_vertice='nombre')
mi_grafo.insert_arist('Coliseo Romano', 'Cristo Redentor', 2500, criterio_vertice='nombre')

mi_grafo.insert_arist('Muralla China', 'Cristo Redentor', 4572, criterio_vertice='nombre')



#Punto C
print('')

arbol_min = mi_grafo.kruskal()

arbol_min_naturales = arbol_min[0].split('-')
peso_total_nat = 0
for nodo in arbol_min_naturales:
    nodo = nodo.split(';')
    peso_total_nat += int(nodo[2])


arbol_min_arqiuitectonicas = arbol_min[1].split('-') 
peso_total_arq = 0
for nodo in arbol_min_arqiuitectonicas:
    nodo = nodo.split(';')
    peso_total_arq += int(nodo[2])

print("ARBOL MINIMO DE MARAVILLAS ARQUITECTONICAS")
print(arbol_min_arqiuitectonicas)
renglon()
print("ARBOL MINIMO DE MARAVILLAS NATURALES")
print(arbol_min_naturales)


#Punto D
renglon()
paises_tipos_de_maravillas = mi_grafo.contar_maravillas()
print('PAISES QUE CUENTAN CON MARAVILLAS ARQUITECTÓNICAS Y NATURALES:')
for pais in paises_tipos_de_maravillas:
    condicion = paises_tipos_de_maravillas[pais]
    if(condicion['arq'] and condicion['nat']):
        
        print(f"- {pais}")

renglon()

#Punto E
paises_con_nat, paises_con_arq = mi_grafo.paises_mas_de_una_maravilla_del_mismo_tipo()

paises_con_maravillas_naturales = Counter(paises_con_nat)
paises_con_maravillas_arquitectonicas = Counter(paises_con_arq)


print('PAISES CON MAS DE UNA MARAVILLA ARQUITECTONICA:')
for pais in paises_con_maravillas_arquitectonicas:
    if(paises_con_maravillas_arquitectonicas[pais] >= 2):
        print(f'- {pais}')

renglon()

print('PAISES CON MAS DE UNA MARAVILLA NATURAL:')
for pais in paises_con_maravillas_naturales:
    if(paises_con_maravillas_naturales[pais] >= 2):
        print(f'- {pais}')  