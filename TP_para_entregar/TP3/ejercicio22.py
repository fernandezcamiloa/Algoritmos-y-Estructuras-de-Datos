# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
# Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

class nodoCola():
    info, sig = None, None


class Cola():

    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__tamnio = 0

    def arribo(self, dato):
        nodo = nodoCola()
        nodo.info = dato

        if self.__final is None:
            self.__frente = nodo
        else:
            self.__final.sig = nodo
        self.__final = nodo

        self.__tamnio += 1

    def atencion(self):
        dato = self.__frente.info

        self.__frente = self.__frente.sig
        if self.__frente is None:
            self.__final = None

        self.__tamnio -= 1
        return dato

    def tamanio(self):
        return self.__tamnio

    def cola_vacia(self):
        return self.__frente is None

    def en_frente(self):
        return self.__frente.info

    def mover_al_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato

    def barrido(self):
        aux = self.__frente
        while (aux is not None):
            print(aux.info)
            aux = aux.sig

    # Funciones ejercicio22

    def personaje_de(self, superheroe):
        aux = self.__frente
        while (aux is not None):
            if (aux.info.nombre_superheroe == superheroe):
                return (aux.info.nombre_personaje)
            aux = aux.sig

    def barrido_personajes_femeninos(self):
        aux = self.__frente
        while (aux is not None):
            if (aux.info.genero == "F"):
                print("-", aux.info.nombre_superheroe)
            aux = aux.sig

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


cola_personajes = Cola()
cola_personajes_aux = Cola()


class personaje:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

    def __str__(self):
        return (f"{self.nombre_personaje}, {self.nombre_superheroe}, {self.genero}")


personajes = [
    {"nombre_personaje": "Tony Stark", "nombre_superheroe": "Iron Man", "genero": "M"},
    {"nombre_personaje": "Steve Rogers",
        "nombre_superheroe": "Capitan America", "genero": "M"},
    {"nombre_personaje": "Carol Danvers",
        "nombre_superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre_personaje": "Natasha Romanoff",
        "nombre_superheroe": "Black Widow", "genero": "F"},
    {"nombre_personaje": "Scott Lang", "nombre_superheroe": "Ant-Man", "genero": "M"},
]


for pers in personajes:
    cola_personajes.arribo(personaje(pers["nombre_personaje"],
                                     pers["nombre_superheroe"],
                                     pers["genero"]))

print("Nombre del personaje de Capitana Marvel:",
      cola_personajes.personaje_de("Capitana Marvel"))

print("----------------------")
print("Personajes Femeninos:")
cola_personajes.barrido_personajes_femeninos()

print("----------------------")
print("Personajes masculinos:")
cola_personajes.barrido_personajes_masculinos()

print("----------------------")
print("Superheroe de Scott Lang:", cola_personajes.superheroe_de("Scott Lang"))

print("----------------------")
print("Superheroes o personajes que empiezan con la letra S:")
cola_personajes.barrido_letra_s()

print("----------------------")
if (cola_personajes.superheroe_de("Carol Danvers") is None):
    print("El personaje Carol Danvers, no se encuentra en la cola")
else:
    print("Superheroe de Carol Danvers:",
          cola_personajes.superheroe_de("Carol Danvers"))
