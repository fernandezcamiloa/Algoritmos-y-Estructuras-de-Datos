def contar_palabra(vector, palabra):
    if not vector:
        return 0
    elif vector[0] == palabra:
        return 1 + contar_palabra(vector[1:], palabra)
    else:
        return contar_palabra(vector[1:], palabra)


palabras = ["heroe", "marvel", "dc", "strange", "heroe"]
palabra_buscada = "heroe"

resultado = contar_palabra(palabras, palabra_buscada)
print(
    f"La palabra '{palabra_buscada}' aparece {resultado} veces.")
