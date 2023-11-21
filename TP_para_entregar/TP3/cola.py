
class Cola():

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):        #agrega un nuevo elemento en el final de la cola
        self.__elementos.append(value)

    def atention(self):             #elimina el primer elemento de la cola
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):                 #devuelve el tamanio de la cola
        return len(self.__elementos)

    def on_front(self):             #devuelve el valor del primer elemento de la cola
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):          #mueve el primer elemento al ultimo lugar de la cola
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux

#    def consultar (self):
#        if self.size() == 0:
#            print ('La cola esta vacia')
#        else: 
#            print (self.__elementos)





