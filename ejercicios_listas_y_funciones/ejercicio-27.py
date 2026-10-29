"""
Ejercicio 27:

Crea una función que calcule el promedio de una lista de números.
"""

# Utilizar la función reduce() requiere importar:
from functools import reduce

def calcular_promedio(pLista_numeros):
    """
    Esta función calcula el promedio de una lista de números.

    Args:
        pLista_numeros (list[int | float]): una lista de números.

    Returns:
        int | float : devuelve el promedio.
    """


    # Calcular el promedio:

    # Control de seguridad para listas vacías(evita división por cero):
    if not pLista_numeros:
        return 0.0

    # 1. Sumar todos los números de la lista para obtener el total.
    suma_total = reduce( lambda acc, num: acc + num, pLista_numeros)
         # Sintaxis: reduce(función_acumuladora, iterable)
         # función_acumuladora: función lambda: "lambda acc, num: acc + num":
         # Dados los parámetros "acc"(un acumulador, en donde se acumula la suma)
         # y "num"(un número de la lista "pLista_numeros" pasada por parámetro),
         # se realiza la suma de todos los números de la lista.

    # 2. Contar cuántos números hay en total en la lista.
    cantidad_numeros = len(pLista_numeros)

    # 3. Dividir la suma total entre la cantidad de números.
    promedio = suma_total / cantidad_numeros

    # Retornar o devolver el resultado:
    return promedio



# PRUEBAS:

lista_1 = [10, 20, 30, 40]
print("Prueba 1 (enteros positivos):", calcular_promedio(lista_1))
# Output: 25.0 ((10 + 20 + 30 + 40) / 4)

lista_2 = [1.5, 2.5, 3.5, 4.5]
print("Prueba 2 (flotantes):", calcular_promedio(lista_2))
# Output: 3.0

lista_3 = [-10, 10, -20, 20]
print("Prueba 3 (positivos y negativos):", calcular_promedio(lista_3))
# Output: 0.0

lista_4 = [42]
print("Prueba 4 (un solo elemento):", calcular_promedio(lista_4))
# Output: 42.0

lista_5 = []
print("Prueba 5 (lista vacía):", calcular_promedio(lista_5))
# Output: 0.0