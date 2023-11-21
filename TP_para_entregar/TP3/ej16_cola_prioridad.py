#16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
#criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
#siguiente situación:
#a. cargue tres documentos de empleados (cada documento se representa solamente con
#un nombre).
#b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#c. cargue dos documentos del staff de TI.
#d. cargue un documento del gerente.
#e. imprima los dos primeros documentos de la cola.
#f. cargue dos documentos de empleados y uno de gerente.
#g. imprima todos los documentos de la cola de impresión.

from cola_prioridad import ColaPrioridad

cola_impresion = ColaPrioridad()

# a. Cargar tres documentos de empleados
print('#a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).')
cola_impresion.arrive("Documentoemp1", 1)
cola_impresion.arrive("Documentoemp2", 1)
cola_impresion.arrive("Documentoemp3", 1)

# b. Imprimir el primer documento de la cola
print('b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).')
primer_documento = cola_impresion.atention()
print("Primer documento:", primer_documento[1])

# c. Cargar dos documentos del staff de TI
print ('c. cargue dos documentos del staff de TI.')
cola_impresion.arrive("DocumentoTI1", 2)
cola_impresion.arrive("DocumentoTI2", 2)

# d. Cargar un documento del gerente
cola_impresion.arrive("DocumentoGerente1", 3)
print ('d. cargue un documento del gerente.')

# e. Imprimir los dos primeros documentos de la cola
print ('e. imprima los dos primeros documentos de la cola.')
for i in range(2):
    print(cola_impresion.atention()[1])

# f. Cargar dos documentos de empleados y uno de gerente
print ('f. cargue dos documentos de empleados y uno de gerente.')
cola_impresion.arrive("Documentoemp4", 1)
cola_impresion.arrive("Documentoemp5", 1)
cola_impresion.arrive("DocumentoGerente2", 3)

# g. Imprimir todos los documentos de la cola de impresión
print ('g. Imprimir todos los documentos de la cola de impresión')
while cola_impresion.size() > 0:
    print (cola_impresion.atention()[1])
