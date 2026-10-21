"""
Ejercicio 4:

Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
"""

def diferencia_entre_listas(pLista_1, pLista_2):
    """
    Esta función calcula la diferencia entre los valores de dos listas numéricas.

    Args:
        pLista_1 (list[int | float]): una lista de números.
        pLista_2 (list[int | float]): otra lista de números.

    Returns:
        list[int | float]: devuelve una lista con la diferencia entre los valores.
    """


    # Creo la lista con la diferencia entre los valores de dos listas
    # y la guardo en una variable: "resultado"
    resultado = list(  map(  lambda x,y: x-y,  pLista_1, pLista_2  )  )

    # "list( ... )" : La función map(), devuelve un objeto mapeado(iterador).
    #                 Lo convierto a lista mediante list()

    # "map(lambda x,y: x-y,  pLista_1, pLista_2)" : map(funcion_a_aplicar, iterable)

    # "lambda x,y: x-y" : utilizo la función lambda para calcular la diferencia entre los valores.
    #                     Sintaxis(lambda) = lambda argumento1, argumento2, ... : expresión_a_retornar


    # Devuelvo / retorno la lista
    return resultado



# PRUEBAS:

lista_1 = [10, 20, 30, 40]
lista_2 = [2, 5, 10, 15]
print(diferencia_entre_listas(lista_1, lista_2))
# [8, 15, 20, 25]


lista_1 = [5.5, -3, 0, 12]
lista_2 = [2.5, -8, 4, 12]
print(diferencia_entre_listas(lista_1, lista_2))
# [3.0, 5, -4, 0]  .... Nota: -3 - (-8) = -3 + 8 = 5


lista_1 = [100, 200, 300, 400, 500]
lista_2 = [10, 20, 30]
print(diferencia_entre_listas(lista_1, lista_2))
# [90, 180, 270]  .... Nota: La función map() se detiene automáticamente
#                            cuando se agota la lista más corta


lista_1 = [7, 14, 21]
lista_2 = [7, 14, 21]
print(diferencia_entre_listas(lista_1, lista_2))
# [0, 0, 0]






