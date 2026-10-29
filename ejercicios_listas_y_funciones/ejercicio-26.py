"""
Ejercicio 26:

Crea una función lambda que calcule el resto de la división entre dos números dados.
"""


# FUNCIÓN LAMBDA:

# Sintaxis(función lambda) = lambda argumentos: expresión

# Operador aritmético para calcular el resto o residuo de una division: "%" (Módulo)
# La función lambda recibe dos parámetros (el dividendo y el divisor) y evalúa la expresión:
resto_division = lambda x, y: x % y



# PRUEBAS:


print("Prueba 1 (resto de 10 % 3):", resto_division(10, 3))
# Output: 1

print("Prueba 2 (resto de 20 % 5 - exacta):", resto_division(20, 5))
# Output: 0

print("Prueba 3 (resto de 3 % 7):", resto_division(3, 7))
# Output: 3

print("Prueba 4 (flotantes(con decimales) 10.5 % 3.0):", resto_division(10.5, 3.0))
# Output: 1.5