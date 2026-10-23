"""
Ejercicio 14:

Crea una función que retorne las palabras de una lista
que comiencen con una letra en específico. Usa la función filter().
"""

def comenzar_letra_especifica(pLista_palabras, pLetra_especifica):
    """
    Esta función, retorna las palabras de una lista que comiencen con una letra en específico.

    Args:
        pLista_palabras (list[str]): una lista de palabras.
        pLetra_especifica (str): una letra.

    Returns:
        list[str]: devuelve las palabras de una lista que comiencen con una letra en específico.
    """


    # IDEA:
    # Filtro la lista de palabras pasada por parámetro mediante la función filter().Para ello,
    # defino una función booleana mediante la función lambda, donde comparo cada palabra
    # de la lista de palabras(parámetro) con la letra específica pasada por parámetro.
    # La función filter() me conservará únicamente aquellas palabras de la lista que cumplan
    # la función booleana y mediante el método list(), obtengo la lista para retornar


    # Defino la función booleana que usaré en la función filter()
    funcion_booleana = lambda palabra: palabra.lower().startswith(pLetra_especifica.lower())
            # Sintaxis(función lambda) = lambda argumento1, argumento2, ...: expresión_a_retornar
            # "palabra" = Hace referencia a cada palabra del iterable "pLista_palabras"
            #             al utilizarla en la función filter()
            # ".lower()" = Para evitar que filter() filtre las mayúsculas y minúsculas
            #           como letras diferentes, convierto todo el texto a minúsculas
            # ".startswith()" = Para verificar el inicio de un texto

    lista_palabras_letra_especifica = list(  filter( funcion_booleana  , pLista_palabras) )
        # Para ver la lista: list( ... )
        # filter(funcion_booleana, iterable)

    return lista_palabras_letra_especifica



# PRUEBAS:


palabras_1 = ["Casa", "coche", "sol", "Cielo", "perro"]
# pLetra_especifica: "c"
print("Prueba 1:", comenzar_letra_especifica(palabras_1, "c"))
# Output: ['Casa', 'coche', 'Cielo']


palabras_2 = ["Python", "Java", "PHP", "JavaScript"]
# pLetra_especifica: "P"
print("Prueba 2:", comenzar_letra_especifica(palabras_2, "P"))
# Output: ['Python', 'PHP']


palabras_3 = ["Manzana", "Pera", "Uva"]
# pLetra_especifica: "z"
print("Prueba 3:", comenzar_letra_especifica(palabras_3, "z"))
# Output: []