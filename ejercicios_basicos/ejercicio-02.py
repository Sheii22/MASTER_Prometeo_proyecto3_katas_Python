"""
Ejercicio 2:

Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().
"""

def doble_valor(pListaNumeros):
    """
    Esta función calcula el doble de cada valor de una lista de números

    Args:
        pListaNumeros (list[int | float]): una lista de números

    Returns:
        devuelve una nueva lista con el doble de cada valor
    """


    # Creo la lista con el doble de cada valor y la guardo en una variable: "numeros"
    numeros = list(  map(  lambda x: x*2, pListaNumeros  )  )

    # "list( ... )" : La función map(), devuelve un objeto mapeado(iterador).
    #                 Lo convierto a lista mediante list()

    # "map(lambda x: x*2, pListaNumeros)" : map(funcion_a_aplicar, iterable)

    # "lambda x: x*2" : utilizo la función lambda para calcular el doble de cada valor.


    # Devuelvo / retorno la lista
    return numeros



# PRUEBAS:

lista_1 = [1, 2, 3, 4, 5]
print(doble_valor(lista_1))
# [2, 4, 6, 8, 10]

lista_2 = [-5, 0, 2.5, 10, -1.2]
print(doble_valor(lista_2))
# [-10, 0, 5.0, 20, -2.4]




