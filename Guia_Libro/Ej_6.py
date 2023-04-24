#Dada una secuencia de caracteres, obtener dicha secuencia invertida.

#cadena = 'hola'
#= 'a' + invertir ('hol')
#= 'a' + 'l' invertir ('ho')


def invertir (cadena):
    if len (cadena) == 0:
        return ''
    else:
        return cadena [-1] + invertir (cadena [-1])
 