"""
Ejercicio 7:

Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
"""

def conversion_a_lista_strings(pLista_tuplas):
    """
    Esta función convierte una lista de tuplas a una lista de strings.

    Args:
        pLista_tuplas (list[tuple]): una lista de tuplas.

    Returns:
        list[str]: devuelve una lista de strings.
    """


    # Convertir la lista de tuplas a una lista de strings:
    lista_str = list(  map( str, pLista_tuplas ) )

    # list(...): Convierte el objeto devuelto por `map()` de nuevo en una lista

    # map(función, iterable): Aplica la función a cada tupla individual contenida en la lista.

    # map(str, tupla): Python aplica `str()` a cada tupla completa,
    #                  por lo que el resultado conserva los paréntesis y las comas


    return lista_str



# PRUEBAS:

lista_tuplas_1 = [("Juan", "Pérez"), ("Ana", "García"), ("Luis", "Martínez")]
print(conversion_a_lista_strings(lista_tuplas_1))
# Salida: ["('Juan', 'Pérez')", "('Ana', 'García')", "('Luis', 'Martínez')"]

lista_tuplas_2 = [(10, 20, 30), (5.5, 2.5)]
print(conversion_a_lista_strings(lista_tuplas_2))
# Salida: ["(10, 20, 30)", "(5.5, 2.5)"]

lista_tuplas_3 = [("Madrid",), ("Barcelona",)]
print(conversion_a_lista_strings(lista_tuplas_3))
# Salida: ["('Madrid',)", "('Barcelona',)"]

lista_tuplas_4 = []
print(conversion_a_lista_strings(lista_tuplas_4))
# Salida: []

