"""
Ejercicio 15:

Crea una función lambda que sume 3 a cada número de una lista dada.
"""


# FUNCIÓN LAMBDA:

# Recibe la lista(pLista_numeros) como parámetro
# y aplica la suma a cada elemento(num) mediante list comprehension
sumar_tres = lambda pLista_numeros: [num + 3 for num in pLista_numeros]
     # Sintaxis(función lambda) = lambda argumentos: expresión
     # "pLista_numeros" = la lista de números(parámetro)
     # "[num + 3 for num in pLista_numeros]" = list comprehension:
     #  Realiza la operación "num + 3" a cada elemento(num) de la lista de números(pLista_numeros)


# PRUEBAS:

lista_1 = [10, 20, 30, 40]
print("Prueba 1:", sumar_tres(lista_1))
# Output: [13, 23, 33, 43]

lista_2 = [5.5, -3, 0, 12]
print("Prueba 2:", sumar_tres(lista_2))
# Output: [8.5, 0, 3, 15]

lista_3 = []
print("Prueba 3:", sumar_tres(lista_3))
# Output: []


