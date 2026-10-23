"""
Ejercicio 12:

Genera una función que, al recibir una frase,
devuelva una lista con la longitud de cada palabra.
Usa la función map().
"""

def longitud_palabras(pFrase):
    """
    Esta función, dada una frase,
    devuelve una lista con la longitud de cada palabra

    Args:
        pFrase (str): una frase.

    Returns:
        list[int]: devuelve una lista con la longitud de cada palabra.
    """


    # Convierto la frase(pasada por parámetro)
    # en una lista de strings, donde cada elemento es una palabra de la frase
    lista_palabras = pFrase.split()

    # Lista con la longitud de cada palabra
    lista_longitud_palabras = list(  map(lambda palabra: len(palabra), lista_palabras) )
           # list(...): Convierte el iterador devuelto por map() en una lista
           # map(función, iterable): Aplica la función a cada tupla individual contenida en la lista.
           # función = función lambda: "lambda palabra: len(palabra)"
           # "lambda palabra: len(palabra)" = lambda argumento1: expresión_a_retornar
           # len(palabra) = longitud de cada palabra

    return lista_longitud_palabras



# PRUEBAS:

frase_1 = "Aprender Python es divertido y útil"
print(longitud_palabras(frase_1))
# Output: [8, 6, 2, 9, 1, 4]

frase_2 = "Supercalifragilisticoespialidoso"
print(longitud_palabras(frase_2))
# Output: [32]

frase_3 = " El lenguaje Python "
print(longitud_palabras(frase_3))
# Output: [2, 8, 6]

frase_4 = ""
print(longitud_palabras(frase_4))
# Output: []

frase_5 = "Ir a la playa es un gran plan"
print(longitud_palabras(frase_5))
# Output: [2, 1, 2, 5, 2, 2, 4, 4]






