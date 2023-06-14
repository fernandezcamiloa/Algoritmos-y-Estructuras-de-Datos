class Bitacora:
    def __init__(self):
        self.pila_misiones = []

    def agregar_mision(self, planeta, capturado, recompensa):
        mision = Mision(planeta, capturado, recompensa)
        self.pila_misiones.append(mision)

    def mostrar_planetas_visitados(self):
        print("Planetas visitados:")
        for mision in self.pila_misiones:
            print(mision.planeta)

    def total_recaudado(self):
        total = sum(mision.recompensa for mision in self.pila_misiones)
        return total

    def mision_han_solo(self):
        for i, mision in enumerate(self.pila_misiones, 1):
            if mision.capturado == "Han Solo":
                return i, mision.planeta


class Mision:
    def __init__(self, planeta, capturado, recompensa):
        self.planeta = planeta
        self.capturado = capturado
        self.recompensa = recompensa


bitacora = Bitacora()

bitacora.agregar_mision("marte", "jaunr", 100)
bitacora.agregar_mision("jupiter", "carlos", 5500)
bitacora.agregar_mision("urano", "Han Solo", 800)


bitacora.mostrar_planetas_visitados()

recaudado = bitacora.total_recaudado()
print(f"Total : {recaudado} creditos ")

mision_han_solo, planeta_han_solo = bitacora.mision_han_solo()
print(
    f"Han Solo fue capturado en la mision {mision_han_solo} en  {planeta_han_solo}")
