"""
Ejercicio 10:

Escribe una función que reciba una lista de números y calcule su promedio.
Si la lista está vacía, lanza una excepción personalizada y maneja el error
adecuadamente.
"""

"""
LANZAR UNA EXCEPCIÓN PERSONALIZADA:

Se define una nueva clase que hereda de la clase base Exception(o de una de sus subclases) 
y se utiliza la palabra clave raise para lanzarla intencionalmente 
cuando no se cumple una condición dentro del flujo del programa.
"""

# 1. DEFINICIÓN DE LA EXCEPCIÓN PERSONALIZADA
class ListaVaciaError(Exception):
    """
    Excepción personalizada
    que se lanza cuando una lista no contiene elementos.
    """
    pass


def calcular_promedio(pLista_numeros):
    """
    Esta función calcula el promedio de una lista de números.

    Args:
        pLista_numeros (list[int | float]): una lista de números.

    Returns:
        int | float: devuelve el promedio.
    """


    # Si la lista está vacía ...
    if not pLista_numeros:
        # ... lanza una excepción personalizada ...
        raise ListaVaciaError("¡ERROR! No es posible calcular el promedio porque la lista está vacía")

    # Calcular promedio
    promedio = sum(pLista_numeros) / len(pLista_numeros)

    return promedio



# PRUEBAS:

lista_1 = [10, 20, 30, 40]
print(calcular_promedio(lista_1))
# Output: 25.0

lista_2 = [5.5, -3, 0, 12]
print(calcular_promedio(lista_2))
# Output: 3.625

# ... y maneja el error adecuadamente(enunciado)

# El código "riesgoso" o propenso a fallos es con esta tercera prueba:
lista_3 = []

# MANEJO DEL ERROR: capturamos la excepción al llamar a la función
try:
    print(calcular_promedio(lista_3))

except ListaVaciaError as error:
    print(f"Prueba 3: Captura controlada del error: {error}")

# Output: Prueba 3: Captura controlada del error:
# ¡ERROR! No es posible calcular el promedio porque la lista está vacía