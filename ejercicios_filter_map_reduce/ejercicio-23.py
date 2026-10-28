"""
Ejercicio 23:

Concatena una lista de palabras. Usa la función reduce().
"""

# Utilizar la función reduce() requiere importar:
from functools import reduce

def concatenar_palabras(pLista_palabras):
    """
    Esta función concatena una lista de palabras.

    Args:
        pLista_palabras (list[str]): una lista de palabras.

    Returns:
        str: devuelve la concatenación de una lista de palabras .
    """


    # Función reduce() - Acumulación a un único valor
    # Requiere importar: "from functools import reduce"
    # Sintaxis: reduce(función_acumuladora, iterable, valor_inicial)
    palabras_concatenadas = reduce(lambda acc, palabra: acc + (" " if acc else "")+ palabra, pLista_palabras, "")
             # (valor_inicial = ""): al concatenar texto, el elemento neutro es la cadena vacía ("")

             # Concatenar con espacio (sin espacio inicial sobrante):
             # "(" " if acc else "")": Si "acc" tiene texto, agrega " " + palabra;
             # si está vacío, solo agrega "palabra"


    return palabras_concatenadas



# PRUEBAS:

lista_1 = ["Hola", "Mundo", "desde", "Python"]
print("Prueba 1:", f"'{concatenar_palabras(lista_1)}'")
# Output: 'Hola Mundo desde Python'

lista_2 = ["Python"]
print("Prueba 2 (una palabra):", f"'{concatenar_palabras(lista_2)}'")
# Output: 'Python'

lista_3 = []
print("Prueba 3 (lista vacía):", f"'{concatenar_palabras(lista_3)}'")
# Output: ''