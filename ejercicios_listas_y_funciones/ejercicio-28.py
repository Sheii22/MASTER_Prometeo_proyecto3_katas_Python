"""
Ejercicio 28:

Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""

def buscar_primer_duplicado(pLista):
    """
    Esta función busca y el primer elemento duplicado de una lista.

    Args:
        pLista (list): Una lista de elementos (números, cadenas, etc.).

    Returns:
        Any | str: El primer elemento duplicado o un mensaje de txto si no hay repetidos.
    """


    # Buscar el primer elemento duplicado:

    # La estructura de datos set(conjunto) NO ADMITE DUPLICADOS.
    # Por lo tanto:

    # Creo un set vacío
    sin_duplicados = set()

    # Recorro la lista pasada por parámetro
    for elemento in pLista:

        # Si el elemento ya ha sido añadido al set ...
        if elemento in sin_duplicados:
            # ...DUPLICADO ENCONTRADO
            return elemento
        # Si el elemento no ha sido añadido al set,
        # y por lo tanto NO ESTÁ DUPLICADO,
        # Añádelo a la lista
        sin_duplicados.add(elemento)

    # Devuelvo un mensaje de txto si no hay repetidos.
    return "No hay duplicados en esta lista"



# PRUEBAS:

lista_1 = [1, 2, 3, 2, 1]
print("Prueba 1 (con duplicados):", buscar_primer_duplicado(lista_1))
# Output: 2

lista_2 = [1, 2, 3, 4, 5]
print("Prueba 2 (sin duplicados):", buscar_primer_duplicado(lista_2))
# Output: No hay duplicados en esta lista

lista_3 = ["manzana", "pera", "manzana", "naranja"]
print("Prueba 3 (cadenas de texto):", buscar_primer_duplicado(lista_3))
# Output: manzana

lista_4 = []
print("Prueba 4 (lista vacía):", buscar_primer_duplicado(lista_4))
# Output: No hay duplicados en esta lista