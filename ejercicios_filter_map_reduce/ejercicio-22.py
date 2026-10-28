"""
Ejercicio 22:

Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
"""

# Utilizar la función reduce() requiere importar:
from functools import reduce

def calcular_producto_total(pLista_numerica):
    """
    Esta función, dada una lista numérica,
    devuelve el producto total de los valores.

    Args:
        pLista_numerica (list[int | float]): una lista de números.

    Returns:
        int | float: devuelve el producto total de los números.
    """


    # Función reduce() - Acumulación a un único valor
    # Requiere importar: "from functools import reduce"
    # Sintaxis: reduce(función_acumuladora, iterable, valor_inicial)
    producto_resultante = reduce(lambda acc, num: acc * num, pLista_numerica, 1)
             # (valor_inicial = 1): el elemento neutro de la multiplicación es el 1
             # funcion_acumuladora_dos_params = Función lambda: "lambda acc, num: acc * num":
             # Dados los parámetros "num"(un número de la lista "pLista_numerica")
             # y "acc"(un acumulador), el resultado del producto se va acumulando


    return producto_resultante



# PRUEBAS:

lista_1 = [5, 10, 0, 3]
print("Prueba 1 (con cero):", calcular_producto_total(lista_1))
# Output: 0

lista_2 = [2, -3, 4, -1]
print("Prueba 2 (negativos):", calcular_producto_total(lista_2))
# Output: 24 (2 * -3 * 4 * -1)

lista_3 = [7]
print("Prueba 3 (un solo elemento):", calcular_producto_total(lista_3))
# Output: 7

lista_4 = [1.5, 2.0, 4.0]
print("Prueba 4 (flotantes):", calcular_producto_total(lista_4))
# Output: 12.0

lista_5 = []
print("Prueba 5 (lista vacía):", calcular_producto_total(lista_5))
# Output: 1