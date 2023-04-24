#22 El problema de la mochila Jedi. Suponga que un Jedi ,Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste, está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
#para encontrarlo;
#c. Utilizar un vector para representar la mochila.



def usar_la_fuerza (lista, buscado):
    if len(lista) == 0:
        return -1
    elif lista[-1] == buscado:
        return len(lista)-1
    else:
        return usar_la_fuerza(lista[0:-1], buscado)

lista = ['bolsa', 'machete', 'sable de luz', 'casco', 'caja']


if 'sable de luz' in lista:
    print('Se encontro el sable despues de sacar', usar_la_fuerza (lista,'sable de luz'), 'objetos')
else:
    print ('El sable no esta')

#prueba git
