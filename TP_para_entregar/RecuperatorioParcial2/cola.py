
class Cola():

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux



#valores = [3, 5, 1, 4, 2]


#for numero in valores:
    #if cola_aux.size() == 0:
    #   cola_aux.arrive(numero)
    #elif numero < cola_aux.on_front():
    #    cola_aux.arrive(numero)
    #    contador = 0
    #    while contador < cola_aux.size()-1:
    #        cola_aux.move_to_end()
    #        contador += 1
    #else:
    #    pass


#while cola_aux.size() > 0:
    #print(cola_aux.atention())


class personaje:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

    def __str__(self):
        return (f"{self.nombre_personaje}, {self.nombre_superheroe}, {self.genero}")


    def personaje_de(self, superheroe):
        cola_aux = self.__frente
        while (cola_aux is not None):
            if (cola_aux.info.nombre_superheroe == superheroe):
                return (cola_aux.info.nombre_personaje)
            cola_aux = aux.sig

    #def barrido_personajes_femeninos(self):
    #    aux = self.__frente
    #    while (aux is not None):
    #        if (aux.info.genero == "F"):
    #            print("-", aux.info.nombre_superheroe)
    #        aux = aux.sig

    #def barrido_personajes_femeninos(self):
    #    for genero in personaje:
    #        if genero == 'M':
    #            cola_aux.arrive (elements)
    #            while cola_aux.size() > 0:
    #print(cola_aux.atention())



#for numero in valores:
    #if cola_aux.size() == 0:
    #   cola_aux.arrive(numero)
    #elif numero < cola_aux.on_front():
    #    cola_aux.arrive(numero)
    #    contador = 0
    #    while contador < cola_aux.size()-1:
    #        cola_aux.move_to_end()
    #        contador += 1
    #else:
    #    pass


#while cola_aux.size() > 0:
    #print(cola_aux.atention())


    def barrido_personajes_masculinos(self):
        aux = self.__frente
        while (aux is not None):
            if (aux.info.genero == "M"):
                print("-", aux.info.nombre_personaje)
            aux = aux.sig

    def superheroe_de(self, personaje):
        aux = self.__frente
        while (aux is not None):
            if (aux.info.nombre_personaje == personaje):
                return (aux.info.nombre_superheroe)
            aux = aux.sig

    def barrido_letra_s(self):
        aux = self.__frente
        while (aux is not None):
            if (aux.info.nombre_personaje[0] == "S" or aux.info.nombre_superheroe[0] == "S"):
                print("-", aux.info)
            aux = aux.sig

