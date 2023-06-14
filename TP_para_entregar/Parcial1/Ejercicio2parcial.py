
class Lista():

    def __init__(self):
        self.__inicio = None
#        self.__tamanio = 0

    def delete(self, value, criterio=None):
        return_value = None
        pos = self.search(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def order_by(self, criterio=None, reverse=False):
        dic_atributos = self.__elements[0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    def barrido_entrenador_mas_tres(self):
        aux = self.__inicio
        while (aux is not None):
            if (aux.info.torneos_ganados > 3):
                print(aux.info)
            aux = aux.sig

    def barrido_lista_lista(self):
        aux = self.__inicio
        while (aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            aux = aux.sig

    def barrido_posterior_1960(self):
        aux = self.__inicio
        while (aux is not None):
            if (aux.info.anio < 1960):
                print(aux.info)
            aux = aux.sig

    def barrido_primer_letra(self, iniciales=[]):
        aux = self.__inicio
        while (aux is not None):
            if (aux.info.namepj[0] in iniciales):
                print(aux.info)
            aux = aux.sig

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while (aux is not None and pos is None):
            if (heroes(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig


# HHHASSSTA ACCA PRIMERRA PARRRTE


class Superheroe:

    def __init__(self, nombreheroe, nombrepj, grupo, anio):
        self.nombreheroe = nombreheroe
        self.nombrepj = nombrepj
        self.grupo = grupo
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} {self.aparicion}, {self.casa}"


lista_heroes = Lista()
heroes = [
    {'namehero': 'iron man', 'namepj': 'Tony Stark',
        'grupo': 'ninguno', 'anio': 1959, },
    {'namehero': 'capitan america', 'namepj': 'Steve Rogers',
        'grupo': 'ninguno', 'anio': 1960, },
    {'namehero': 'dr. strange', 'namepj': 'Stephen Strange',
        'grupo': 'ninguno', 'anio': 2005, },
    {'namehero': 'spiderman', 'namepj': 'Peter Parker',
        'grupo': 'ninguno', 'anio': 1990, },
    {'namehero': 'Capitana Marvel', 'namepj': 'Juana Molina',
        'grupo': 'ninguno', 'anio': 1999, },
]


#!                       punto A
dato = lista_heroes.busqueda('Capitana Marvel')
if dato:
    print(
        f'el superheroe {dato.info.namehero} su nombre es {dato.info.namepj}')
else:
    print('el superheroe no esta en la lista')

 #!                 punto D
print()
lista_heroes.barrido_posterior_1960()

#!                        punto E
dato = lista_heroes.busqueda('Vlanck Widow'.namehero(), 'nombre')
if dato:
    dato.info.namehero = 'Black Widow'
    print(f'el superheroes {dato.info.nombre} fue modificado')
else:
    print('el superheroe no esta en la lista')

#                punto G
print()
lista_heroes.barrido_primer_letra(['C', 'P', 'S'])
