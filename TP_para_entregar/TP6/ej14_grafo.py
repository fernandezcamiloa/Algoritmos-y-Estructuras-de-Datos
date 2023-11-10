#14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
#tareas:
#a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#baño 1, baño 2, habitación 1, habitación 2, sagrafola de estar, terraza, patio;
#b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
#es la distancia entre los ambientes, se debe cargar en metros;
#c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#para conectar todos los ambientes;
#d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#determinar cuántos metros de cable de red se necesitan para conectar el router con el
#Smart Tv.

from grafo import Grafo

mi_grafo = Grafo(dirigido=False)

mi_grafo.insert_vertice('cocina') 
mi_grafo.insert_vertice('comedor') 
mi_grafo.insert_vertice('cochera') 
mi_grafo.insert_vertice('quincho') 
mi_grafo.insert_vertice('baño 1') 
mi_grafo.insert_vertice('baño 2') 
mi_grafo.insert_vertice('habitacion 1') 
mi_grafo.insert_vertice('habitacion 2') 
mi_grafo.insert_vertice('sala de estar') 
mi_grafo.insert_vertice('terraza')
mi_grafo.insert_vertice('patio')

mi_grafo.insert_arist('cocina', 'comedor', 6)
mi_grafo.insert_arist('cocina', 'cochera', 12)
mi_grafo.insert_arist('cocina', 'quincho', 18)
mi_grafo.insert_arist('cocina', 'baño 1', 9)
mi_grafo.insert_arist('cocina', 'baño 2', 16)

mi_grafo.insert_arist('comedor', 'patio', 8)
mi_grafo.insert_arist('comedor', 'terraza', 10)
mi_grafo.insert_arist('comedor', 'sala de estar', 11)
mi_grafo.insert_arist('comedor', 'habaitacion 2', 1)

mi_grafo.insert_arist('cochera', 'quincho', 3)
mi_grafo.insert_arist('cochera', 'baño 1', 14)
mi_grafo.insert_arist('cochera', 'terraza', 7)

mi_grafo.insert_arist('quincho', 'habitacion 1', 2)

mi_grafo.insert_arist('baño 1', 'patio', 4)

mi_grafo.insert_arist('baño 2', 'terraza', 13)
mi_grafo.insert_arist('baño 2', 'habitacion 1', 22)

mi_grafo.insert_arist('habitacion 1', 'habitacion 2', 27)

mi_grafo.insert_arist('habitacion 2', 'sala de estar', 25)

mi_grafo.insert_arist('sala de estar', 'patio', 30)

arbol_min = mi_grafo.kruskal()


arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])



print("PUNTO C")
print(arbol_min)
print(f"La cantidad de cables minima necesaria para conectar todos los ambientes es {peso_total} metros")



print(" ")
print("PUNTO D")

if(mi_grafo.existe_paso("habitacion 1", "sala de estar")):
    resultados = mi_grafo.dijkstra ("habitacion 1")
    camino = mi_grafo.camino(resultados, "habitacion 1", "sala de estar")
    print("El camino más corto entre la habitación 1 y la sala de estar es:", camino['camino'])

    print("La cantidad minima de cable necesaria para conectar el router con el smart tv es de", camino['costo'], "metros")

else:
    print("No existe paso desde habitacion 1 hasta saka de estar")
