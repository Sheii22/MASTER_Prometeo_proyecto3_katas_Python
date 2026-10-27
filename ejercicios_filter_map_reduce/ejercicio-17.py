"""
Ejercicio 17:

Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().
"""

# Utilizar la función reduce() requiere importar:
from functools import reduce

def numero_correspondiente(pLista_digitos):
    """
    Esta función, dada una lista de dígitos,
    devuelve el número correspondiente.

    Args:
        pLista_digitos (list[int]): una lista de dígitos.

    Returns:
        int: devuelve un número.
    """


    # Función reduce() - Acumulación a un único valor
    # Requiere importar: "from functools import reduce"
    # Sintaxis: reduce(funcion_acumuladora_dos_params, iterable)

    # Función lambda: multiplica el acumulador por 10 y le suma el siguiente dígito:
    # Ejemplo:
    #     1. Toma el primer elemento: 2.
    #     2. Multiplica por 10 y suma el siguiente dígito: 2 * 10 + 3 = 23.
    #     3. Repite con el siguiente dígito: 23 * 10 + 4 = 234`.
    numero = reduce(lambda acumulador, digito: acumulador * 10 + digito, pLista_digitos, 0)
                   # Añado '0' como tercer argumento de reduce() para manejar listas vacías

    return numero



# PRUEBAS:

lista_1 = [1, 0, 0, 4]
print("Prueba 1:", numero_correspondiente(lista_1))
# Output: 1004

lista_2 = [9]
print("Prueba 2:", numero_correspondiente(lista_2))
# Output: 9

lista_3 = [0, 5, 2]
print("Prueba 3:", numero_correspondiente(lista_3))
# Output: 52

lista_4 = [0, 0, 0]
print("Prueba 4:", numero_correspondiente(lista_4))
# Output: 0

lista_5 = []
print("Prueba 5:", numero_correspondiente(lista_5))
# Output: 0