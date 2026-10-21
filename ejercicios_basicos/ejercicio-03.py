"""
Ejercicio 3:

Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
La función debe devolver una lista con todas las palabras de la lista original
que contengan la palabra objetivo.
"""

def contiene_palabra_objetivo(pListaPalabras, pPalabraObjetivo):
    """
    Esta función devuelve una lista con todas las palabras de la lista original,
    que contengan la palabra objetivo.

    Args:
        pListaPalabras (list[str]): una lista de palabras.
        pPalabraObjetivo (str): una palabra.

    Returns:
        devuelve una lista con todas las palabras de la lista original
        que contengan la palabra objetivo.
    """


    # Creo una lista vacía. La cual retornaré.
    lista_final = []

    # Recorro la lista de palabras que me han pasado por parámetro
    for palabra in pListaPalabras:


        # Si encuentro la palabra objetivo en la lista . . .

        # (Para comprobar la pertenencia o inclusión en Python se utiliza el operador "in".
        # El enunciado pide buscar que la palabra objetivo sea una subcadena dentro de cada palabra)
        if pPalabraObjetivo.lower() in palabra.lower():
           # Convierto ambas palabras a minúsculas con .lower() para compararlas.
           # Ya que Python diferencia entre mayúsculas y minúsculas,
           # dos cadenas idénticas en letra pero con distinta capitalización darán `False`.

            #  . . . añado la palabra actual a la nueva lista
            lista_final.append(palabra)

    return lista_final



# PRUEBAS:


lista_palabras_1 = ["mar", "marea", "mariposa", "sol", "pescado", "marina"]
palabra_objetivo_1 = "mar"
print(contiene_palabra_objetivo(lista_palabras_1, palabra_objetivo_1))
# ["mar", "marea", "mariposa", "marina"]


lista_palabras_2 = ["programación", "python", "procesador", "función", "proyecto", "variable"]
palabra_objetivo_2 = "pro"
print(contiene_palabra_objetivo(lista_palabras_2, palabra_objetivo_2))
# ["programación", "procesador", "proyecto"]


lista_palabras_3 = ["python", "PyCharm", "Pytorch", "javascript", "ruby"]
palabra_objetivo_3 = "py"
print(contiene_palabra_objetivo(lista_palabras_3, palabra_objetivo_3))
# ["python", "PyCharm", "Pytorch"]


lista_palabras_4 = ["manzana", "pera", "plátano", "uva"]
palabra_objetivo_4 = "limón"
print(contiene_palabra_objetivo(lista_palabras_4, palabra_objetivo_4))
# []




