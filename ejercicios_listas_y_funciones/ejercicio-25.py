"""
Ejercicio 25:

Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""

def contar_numero_de_caracteres(pTxt):
    """
    Esta función cuenta el número de caracteres en una cadena de texto dada.

    Args:
        pTxt (str): una cadena de texto.

    Returns:
        int : devuelve el número de caracteres.
    """


    # La función incorporada que devuelve la cantidad de caracteres de un string es: "len()":
    # Sintaxis: len(elemento)
    numero_caracteres = len(pTxt)

    return numero_caracteres



# PRUEBAS:

texto_1 = "Hola Mundo"
print(f"Prueba 1 ('{texto_1}'):", contar_numero_de_caracteres(texto_1))
# Output: 10

texto_2 = ""
print("Prueba 2 (cadena vacía):", contar_numero_de_caracteres(texto_2))
# Output: 0

texto_3 = "¡Python 3.12!"
print(f"Prueba 3 ('{texto_3}'):", contar_numero_de_caracteres(texto_3))
# Output: 13

texto_4 = "   "
print("Prueba 4 (3 espacios):", contar_numero_de_caracteres(texto_4))
# Output: 3