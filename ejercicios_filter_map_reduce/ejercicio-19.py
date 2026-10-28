"""
Ejercicio 19:

Crea una función lambda que filtre los números impares de una lista dada.
"""


# FUNCIÓN LAMBDA:

# filtro los números impares utilizando list comprehension dentro de la función lambda:

                                     # list comprehension:
num_impares = lambda pLista_numeros: [num for num in pLista_numeros if num % 2 != 0]
     # Sintaxis(función lambda) = lambda argumentos: expresión

     # Números pares: num % 2 == 0  - Números IMPARES: num % 2 != 0

     # list comprehension: [num for num in pLista_numeros if num % 2 != 0]:
     # Para filtrar elementos en un list comprehension, pongo la variable "num" al inicio
     # y coloco la condición dentro de un if al final(if num % 2 != 0).
     # "for num in pLista_numeros": mediante un for recorro la lista "pLista_numeros",
     # donde la variable-índice "num" hará referencia a cada elemento de la lista



# PRUEBAS:


lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Prueba 1:", num_impares(lista_1))
# Output: [1, 3, 5, 7, 9]

lista_2 = [2, 4, 6, 8]
print("Prueba 2 (solo pares):", num_impares(lista_2))
# Output: []

lista_3 = [-5, -4, -3, -2, -1, 0]
print("Prueba 3 (negativos):", num_impares(lista_3))
# Output: [-5, -3, -1]

lista_4 = []
print("Prueba 4 (lista vacía):", num_impares(lista_4))
# Output: []




