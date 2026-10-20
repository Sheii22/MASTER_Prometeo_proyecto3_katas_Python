"""
Ejercicio 1:

Escribe una función que reciba una cadena de texto como parámetro
y devuelva un diccionario con las frecuencias de cada letra en la cadena.
Los espacios no deben ser considerados.
"""

def frecuencias_letras(pTxt):
    """
    Esta función calcula la frecuencias de cada letra en una cadena de caracteres(string).

    Args:
        pTxt: una cadena de texto.

    Returns:
        diccionario: Un diccionario que contiene como claves cada letra(char)
        de la cadena de caracteres, y como valores las frecuencias de cada letra.
    """


    # Convierto todo el texto a minúsculas,
    #  porque no quiero que mayúsculas y minúsculas
    # las cuente como letras diferentes.
    pTxt = pTxt.lower()

    # Creo un diccionario vacío. El cual retornaré
    dicc_frecuencia_letras = dict()

    # Recorro el string(pTxt),
    # guardando cada letra como clave del diccionario
    # y calculando los valores de cada letra o clave
    # mediante el método count()

    # Recorro el string(pTxt)
    for letra in pTxt:

        # Enunciado: "Los espacios no deben ser considerados"
        # Si la letra actual NO es un espacio:
        if letra != " ":
            # 1. Añádeme la letra actual como clave al dicionario
            # 2. Calcúlame el número de frecuencias de dicha letra
            # y añádeme dicha frecuencia como valor
            clave = letra.lower()
            valor = pTxt.count(letra)
            dicc_frecuencia_letras[clave] = valor

    # Devuelvo / retorno el dicionario
    return dicc_frecuencia_letras



# PRUEBAS:

prueba_1 = frecuencias_letras("python")
print(prueba_1)
# {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

prueba_2 = frecuencias_letras("Estoy aprendiendo a programar en python")
print(prueba_2)
# {'e': 4, 's': 1, 't': 2, 'o': 4, 'y': 2, 'a': 4, 'p': 3, 'r': 4, 'n': 4, 'd': 2, 'i': 1, 'g': 1, 'm': 1, 'h': 1}


