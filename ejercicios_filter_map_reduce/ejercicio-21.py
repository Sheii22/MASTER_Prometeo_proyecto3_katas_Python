"""
Ejercicio 21:

Crea una función que calcule el cubo de un número dado mediante una función lambda.
"""

# FUNCIÓN LAMBDA:
# Son funciones anónimas(sin nombre explícito "def") que se definen en una sola instrucción.
# Sintaxis(función lambda) = lambda argumentos: expresión
# Recibe un número mediante el parámetro "pNumero" y calcula su cubo:
# "pNumero elevado a 3" (pNumero ** 3)
calcular_cubo = lambda pNumero: pNumero ** 3
   # Nota: al asignar la función lambda a la variable "calcular_cubo"
   # ("calcular_cubo = lambda pNumero: pNumero ** 3"),
   # "calcular_cubo" actúa directamente como la función.



# PRUEBAS:

num_1 = 3
print(f"Prueba 1 (cubo de {num_1}):", calcular_cubo(num_1))
# Output: 27 (3 * 3 * 3)

num_2 = 0
print(f"Prueba 2 (cubo de {num_2}):", calcular_cubo(num_2))
# Output: 0 (0 * 0 * 0)

num_3 = -3
print(f"Prueba 3 (cubo de {num_3}):", calcular_cubo(num_3))
# Output: -27 ((-3) * (-3) * (-3))

num_4 = 1.5
print(f"Prueba 4 (cubo de {num_4}):", calcular_cubo(num_4))
# Output: 3.375 (1.5 * 1.5 * 1.5)

num_5 = 10
print(f"Prueba 5 (cubo de {num_5}):", calcular_cubo(num_5))
# Output: 1000 (10 * 10 * 10)