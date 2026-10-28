"""
Ejercicio 20:

Para una lista con elementos de tipo integer y string,
obtén una nueva lista solo con los valores int.
Usa la función filter().
"""

def filtrar_valores_int(pLista):
    """
    Esta función, dada una lista,
    devuelve los valores int.

    Args:
        pLista (list[integer | str]): una lista con elementos de tipo integer y string.

    Returns:
        list[integer]: devuelve una nueva lista solo con los valores int.
    """


    # Función filter() - Selección y filtrado booleano
    # Sintaxis: filter(funcion_booleana, iterable)
    # Utilizo una función lambda para definir la función booleana pasada por parámetro en filter():
    valores_int = list( filter( lambda elemento: type(elemento) == int , pLista) )
                  # Para ver la lista: list()

                  # Sintaxis(función lambda) = lambda argumentos: expresión
                  # Función lambda: "lambda elemento: type(elemento) == int"
                  # "Elemento" es el parámetro, el cual hace referencia a cada elemento
                  # de la lista / iterable "pLista". Si dicho elemento es de tipo int,
                  # es decir, cumple la condición(type(elemento) == int) este elemento
                  # es incluido a la nueva lista: "valores_int"

                  # Obtener el tipo de dato de una variable: "type()"
                  # Es una función incorporada. Sintaxis: type(elemento)

    # Retorno la lista generada mediante la función filter()
    return valores_int



# PRUEBAS:

lista_1 = [1, "hola", 25, "Python", 100, "mundo", 0]
print("Prueba 1:", filtrar_valores_int(lista_1))
# Output: [1, 25, 100, 0]

lista_2 = ["manzana", "20", "3.14", "False"]
print("Prueba 2 (solo cadenas):", filtrar_valores_int(lista_2))
# Output: []

lista_3 = [10, 20, 30]
print("Prueba 3 (solo enteros):", filtrar_valores_int(lista_3))
# Output: [10, 20, 30]

lista_4 = []
print("Prueba 4 (lista vacía):", filtrar_valores_int(lista_4))
# Output: []