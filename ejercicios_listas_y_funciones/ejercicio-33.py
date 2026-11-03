"""
Ejercicio 33:

Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""


# FUNCIÓN LAMBDA:

# Sintaxis(función lambda) = lambda argumentos: expresión
                                             # list comprehension:
sumar_elementos = lambda pLista_1, pLista_2: [ x + y for x, y in zip(pLista_1, pLista_2)]
                     # Uso la función zip() dentro de la list comprehension
                     # para recorrer ambas listas a la vez.
                     # Función zip(): combina elementos de dos o más iterabes,
                     # agrupándolos en tuplas según su posición(índice).
                     # En la list comprehension, desempaqueto esa tupla
                     # escribiendo "for x, y in zip(...)".



# PRUEBAS:

lista_a = [1, 2, 3, 4]
lista_b = [10, 20, 30, 40]
print("Prueba 1 (mismo tamaño):", sumar_elementos(lista_a, lista_b))
# Output: [11, 22, 33, 44]

lista_c = [1.5, -2, 3.0]
lista_d = [0.5, 2, 1.0]
print("Prueba 2 (decimales y negativos):", sumar_elementos(lista_c, lista_d))
# Output: [2.0, 0, 4.0]

lista_e = [10, 20, 30, 40, 50]
lista_f = [1, 2]
print("Prueba 3 (diferente tamaño):", sumar_elementos(lista_e, lista_f))
# Output: [11, 22]

print("Prueba 4 (listas vacías):", sumar_elementos([], []))
# Output: []