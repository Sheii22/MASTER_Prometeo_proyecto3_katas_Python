"""
Ejercicio 6:

Escribe una función que calcule el factorial de un número de manera recursiva.
"""

def calcular_factorial(pNumero):
    """
    Esta función calcula el factorial de un número entero no negativo.

    Args:
        pNumero (int): un número entero no negativo.

    Returns:
        Devuelve el factorial de un número entero no negativo.
    """


    # Si el número es decimal
    if isinstance(pNumero, float):
        # Lo convierto a entero
        pNumero = int(pNumero)
        # Y vuelvo a llamar a la función
        return calcular_factorial(pNumero)

    # Si el número es negativo
    elif pNumero < 0:
         return "No se puede calcular el factorial de un número negativo"

    # Número entero y no negativo
    else:

        # RECURSIVIDAD

        # Factorial: n! = n*(n-1)!

        # CASO BASE: detiene el bucle
        #     0! = 1          1! = 1
        if pNumero == 0 or pNumero == 1:
            return 1
        # CASO RECURSIVO: la función se llama a sí misma hasta llegar al caso base
        # n! = n*(n-1)!
        else:
            return pNumero * calcular_factorial(pNumero-1)



# PRUEBAS:

print(calcular_factorial(4.2))
# Resultado esperado: factorial de 4: 4! = 24

print(calcular_factorial(-3))
# Resultado esperado: "No se puede calcular el factorial de un número negativo"

print(calcular_factorial(0))
# Resultado esperado: 1 (Por definición matemática 0! = 1)

print(calcular_factorial(1))
# Resultado esperado: 1

print(calcular_factorial(6))
# Resultado esperado: 720 (6 * 120)





