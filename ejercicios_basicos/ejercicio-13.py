"""
Ejercicio 13:

Genera una función que, para un conjunto de caracteres,
devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
Las letras no pueden estar repetidas. Usa la función map().
"""

def letras_mayus_minus(pConjunto_de_caracteres):
    """
    Esta función, dado un conjunto de caracteres,
    devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas

    Args:
        pConjunto_de_caracteres (set): un conjunto de caracteres.

    Returns:
        list[tuple]: devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas.
    """


    # Me aseguro de que no haya elementos repetidos
    conjunto_caracteres = set(pConjunto_de_caracteres)

    lista_tuplas = list(  map( lambda letra: (letra.upper(), letra.lower()), conjunto_caracteres ) )
         # list(...): Convierte el objeto devuelto por map() en una lista

         # map(función, iterable): Aplica la función a cada elemento del iterable

         # Sintaxis(lambda ) = lambda argumento1, argumento2, ...: expresión_a_retornar
         # "lambda letra: (letra.upper(), letra.lower())" = Para que la función lambda
         # me devuelva una tupla, envuelvo los valores entre paréntesis y separados por una coma.

         # "letra.upper()" = Convierte todos los caracteres de la cadena a mayúsculas
         # "letra.lower()" = Convierte todos los caracteres de la cadena a minúsculas

    return lista_tuplas



# PRUEBAS:

conjunto_1 = {'a', 'b', 'c'}
print("Prueba 1:", letras_mayus_minus(conjunto_1))
# Output: [('A', 'a'), ('C', 'c'), ('B', 'b')] (el orden en un set puede variar)

cadena_2 = "palabra"
print("Prueba 2:", letras_mayus_minus(cadena_2))
# Output: [('P', 'p'), ('A', 'a'), ('R', 'r'), ('B', 'b'), ('L', 'l')]
