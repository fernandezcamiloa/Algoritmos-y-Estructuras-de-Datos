
from lista import Lista as ListaSimple


def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1][0], criterio):
            self.__elements.append([value, ListaSimple()])
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0][0], criterio):
            self.__elements.insert(0, [value, ListaSimple()])
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index][0], criterio):
                index += 1
            self.__elements.insert(index, [value, ListaSimple()])

    def search(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle][0], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle][0], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

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
            print(value[0])
            print('Sublista ----------------')
            value[1].barrido()

    def barrido_entrenadores(self):
        for value in self.__elements:
            print(value[0])
            print('Lista de Pokemons:')
            value[1].barrido()
            print()

    def barrido_cantidad_torneos_ganados(self, cantidad_victorias):
        for value in self.__elements:
            if value[0].ct_ganados > cantidad_victorias:
                print(value[0]) 

    def barrido_porcentaje_batallas_79(self):
        for value in self.__elements:
            porcentaje_79 = (value[0].cb_ganadas  / (value[0].cb_ganadas + value[0].cb_perdidas)) * 100
            if (porcentaje_79 > 79):
                print(value[0].nombre)

    def order_by(self, criterio=None, reverse=False):
        dic_atributos = self.__elements[0][0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value

    # def set_value(self, value, new_value, criterio=None):
    #     pos = self.search(value, criterio)
    #     if pos is not None:
    #         value = self.delete(value)
    #         self.insert(new_value, criterio)


class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        # self.materia = None

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.edad}'


class Materia():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f'{self.nombre}'
# class Producto():

#     def __init__(self, id, tipo):
#         self.id = id
#         self.tipo = tipo

#     def __str__(self):
#         return f'{self.id} - {self.tipo}'


# lista_prueba = Lista()
# lista_valores = []

# def cargar_lista(lista_aux):
#     personas = [
#         ['Juana', 'Gomez', 34],
#         ['Mario', 'Impini', 47],
#         ['Laurato', 'Perez', 19],
#         ['Leo', 'Impini', 33],
#         ['Maria', 'Sittoni', 7],
#         ['Julieta', 'Alem', 20],
#     ]
#     for persona in personas:
#         lista_valores.append(Persona(persona[0], persona[1], persona[2]))
#         lista_prueba.insert(Persona(persona[0], persona[1], persona[2]), 'apellido')

# def comienza_con(lista_aux, letra):
#     print()
#     print('prueba')
#     for i in range(lista_aux.size()):
#         persona = lista_aux.get_element_by_index(i)
#         if persona.nombre.startswith(letra):
#             print(persona)
#     print('prueba')
#     print()


# cargar_lista(lista_prueba)


# comienza_con(lista_prueba, 'Mar')
# persona1.
# print(criterio_comparacion(persona1, 'apellido'))

# print(persona1.__dict__)


# persona = Persona('perez', 'juan', 13)
# lista_prueba.insert(persona, 'nombre')
# persona = Persona('alba', 'ana', 13)
# lista_prueba.insert(persona, 'nombre')
# persona = Persona('nose', 'matias', 13)
# lista_prueba.insert(persona, 'nombre')


# print(lista_prueba.get_element_by_index(0)[0])
# print(lista_prueba.get_element_by_index(0)[1].size())

# pos = lista_prueba.search('perez', 'nombre')
# print(pos)
# if pos:
#     value = lista_prueba.get_element_by_index(pos)
#     # print(value[0])
#     value[1].insert(Materia('programacion 1', 9), 'nota')
#     value[1].insert(Materia('programacion 2', 10), 'nota')

# pos = lista_prueba.search('nose', 'nombre')
# # print(pos)
# if pos:
#     value = lista_prueba.get_element_by_index(pos)
#     # print(value[0])
#     value[1].insert(Materia('ingenieria', 9), 'nota')
#     value[1].insert(Materia('ingles', 8), 'nota')

# pos = lista_prueba.search('alba', 'nombre')
# print(pos)
# if pos > -1:
#     value = lista_prueba.get_element_by_index(pos)
#     # print(value[0])
#     value[1].insert(Materia('matematica', 7), 'nota')

# # lista_prueba.barrido()

# pos = lista_prueba.search('nose', 'nombre')
# if pos:
#     pos_aux = lista_prueba.get_element_by_index(pos)[1].search(8, 'nota')
#     if pos_aux is not None:
#         print('cursa la materia')
#     else:
#         print('no cursa la materia')


# lista_prueba.insert(prod1, 'id')
# lista_prueba.insert(prod2, 'id')
# lista_prueba.insert(persona1, 'apellido')
# lista_prueba.insert(persona2, 'apellido')
# lista_prueba.insert(persona3, 'apellido')
# lista_prueba.insert(persona4, 'apellido')
# lista_prueba.insert(persona5, 'apellido')
# lista_prueba.insert(persona6, 'apellido')

# lista_prueba.barrido()
# print()
# for i in range(lista_prueba.size()-1, -1, -1):
#     print(lista_prueba.get_element_by_index(i))
# lista_prueba.insert(5)
# lista_prueba.insert(3)
# lista_prueba.insert(1)
# lista_prueba.insert(8)
# lista_prueba.insert(4)
# lista_prueba.insert(6)
# lista_prueba.insert(2)
# lista_prueba.insert(3)
# lista_prueba.insert(7)
# lista_prueba.insert(1)

# lista_prueba.set_value(5, 9)

# lista_prueba.barrido()
# print()
# position = lista_prueba.search('Sittoni', 'apellido')
# if position:
#     lista_prueba.get_element_by_index(position).apellido = 'Alvarez'
#     lista_prueba.order_by('apellido')
    # print('edad de persona', lista_prueba.get_element_by_index(position).edad)
# persona = lista_prueba.delete('Sittoni', 'apellido')
# print('persona eliminada', persona)
# persona.apellido = 'Alvarez'
# lista_prueba.insert(persona, 'apellido')
# print()
# lista_prueba.barrido()
# print(lista_prueba.get_element_by_index(position))
# lista_prueba.order_by()
# print(lista_prueba.search('Leo', 'nombre'))

# lista_valores = [5, 1, 5, 0, 10, 7]
#
# print(lista_valores)

# print(lista_prueba.delete(1))
# print()
# lista_prueba.barrido()
# print(lista_prueba.__elements)
# # print(lista_prueba.delete(4))
# # print(lista_prueba.__elements)
# print(lista_prueba.delete(3))
# print(lista_prueba.__elements)

# def contarmayoresde18(lista)
#     print('dentro de la funcion')
#     lista.barrido()

# contarmayoresde18(lista_prueba)
# lista_prueba.barrido()

# print(lista_prueba.get_element_by_value(4))
# print(lista_prueba.get_element_by_value(10))

# print(lista_prueba.get_element_by_index(4))
# print(lista_prueba.get_element_by_index(100))

# lista_value = ['a', 'h', 'z', 'd', 'f']

# for index, value in enumerate(lista_value):
#     if value == 'c':
#         print(f'lo encontre en la posicion {index}')
#     print(index, value)
# def apellido_nombre(item):
#     print(criterio)
#     return item.apellido+item.nombre

# def nombre(item):
#     return item.nombre

# def apellido(item):
#     return item.apellido

# def edad(item):
#     return item.edad

# lista_valores.sort(key=apellido_nombre)
# print()
# for persona in lista_valores:
#     print(persona)
