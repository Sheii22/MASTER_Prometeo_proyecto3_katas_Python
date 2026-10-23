"""
Ejercicio 16:

Escribe una función que tome una cadena de texto y un número entero n como parámetros
y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().
"""

def palabras_mas_largas(pTxt, n):
    """
    Esta función, dada una cadena de texto y un número entero n,
    devuelve una lista de todas las palabras que sean más largas que n.

    Args:
        pTxt (str): una cadena de texto.
        n (int): un número entero.

    Returns:
        list[str]: devuelve una lista de todas las palabras que sean más largas que n.
    """


    # Convertir la cadena de texto pasada por parámetro(pTxt) a lista de palabras
    lista_palabras = pTxt.split()

    # Defino la función booleana(mediante una función lambda) que voy a pasar por la función filter()
    funcion_booleana =  lambda palabra: len(palabra) > n

    # Funcionamiento de la función booleana en la función filter():
    # Dado el parámetro "palabra", el cual hace referencia a cada elemento
    # del iterable lista_palabras, genero una lista con los elementos
    # que cumplen la condición: "len(palabra) > n". Es decir, que la longitud
    # de la "palabra" sea mayor que el número entero "n"

    palabras_largas = list( filter(funcion_booleana, lista_palabras) )
        # Para ver la lista: list( ... )
        # filter(funcion_booleana, iterable)


    return palabras_largas



# PRUEBAS:

txt_1 = "Hola mundo Python"
print("Prueba 1 (n = 4):", palabras_mas_largas(txt_1, 4))
# Output: ['mundo', 'Python'] ('Hola' tiene 4 letras, por lo que se excluye al requerir > 4)

txt_2 = "Aprender a programar es genial"
print("Prueba 2 (sin coincidencias, n = 8):", palabras_mas_largas(txt_2, 8))
# Output: ['programar']

txt_3 = "Python JavaScript TypeScript"
print("Prueba 3 (todas coinciden, n = 2):", palabras_mas_largas(txt_3, 2))
# Output: ['Python', 'JavaScript', 'TypeScript']

txt_4 = ""
print("Prueba 4 (cadena vacía, n = 3):", palabras_mas_largas(txt_4, 3))
# Output: []