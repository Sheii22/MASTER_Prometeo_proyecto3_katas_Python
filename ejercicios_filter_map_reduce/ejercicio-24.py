"""
Ejercicio 24:

Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""

# Utilizar la función reduce() requiere importar:
from functools import reduce

def calcular_diferencia_total(pLista):
    """
    Esta función calcula la diferencia total en los valores de una lista.

    Args:
        pLista (list[int | float]): una lista de números.

    Returns:
        int | float: devuelve la diferencia total de una lista de números.
    """


    # Enunciado: "Calcula la diferencia total": se toma el primer elemento como punto de partida
    # y se le resta el segundo; al resultado obtenido se le resta el tercero,
    # y así sucesivamente hasta procesar toda la lista

    # Función reduce() - Acumulación a un único valor
    # Requiere importar: "from functools import reduce"
    # Sintaxis: reduce(función_acumuladora, iterable)
    diferencia_total = reduce(lambda acc, num: acc - num, pLista)
                   # función_acumuladora: mediante una función lambda:
                   # "lambda acc, num: acc - num": dados los parámetros:
                   # "acc"(un acumulador donde se almacena la operación que finalmente se retornará)
                   # y "num"(cada número del iterable recibido como parámetro: "pLista"), calcula
                   # la diferencia total(detallada paso a paso en el comentario de arriba)


    return diferencia_total



# PRUEBAS:

lista_1 = [100, 20, 10, 5]
print("Prueba 1 (estándar):", calcular_diferencia_total(lista_1))
# Output: 65 ((100 - 20) - 10) - 5

lista_2 = [50, -10, 5]
print("Prueba 2 (con negativos):", calcular_diferencia_total(lista_2))
# Output: 55 (50 - (-10)) - 5 = 60 - 5 = 55

lista_3 = [42]
print("Prueba 3 (un solo elemento):", calcular_diferencia_total(lista_3))
# Output: 42

lista_4 = [10.5, 2.5, 1.0]
print("Prueba 4 (flotantes):", calcular_diferencia_total(lista_4))
# Output: 7.0