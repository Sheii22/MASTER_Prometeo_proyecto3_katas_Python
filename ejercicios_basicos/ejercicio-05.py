"""
Ejercicio 5:

Escribe una función que tome una lista de números como parámetro
y un valor opcional nota_aprobado (por defecto 5).
La función debe calcular la media de los números en la lista
y determinar si la media es mayor o igual que nota_aprobado.
Si es así, el estado será "aprobado"; de lo contrario, "suspenso".
La función debe devolver una tupla que contenga la media y el estado.
"""

def calcular_media_y_estado(pLista_Numeros, nota_aprobado = 5):
    """
    Esta función calcula la media de los números de una lista dada
    y determinar si la media es mayor o igual que nota_aprobado.

    Args:
        pLista_Numeros (list[int | float]): una lista de números.
        nota_aprobado (int | float): un valor opcional(por defecto 5).

    Returns:
        Tuple[int | float, str]: devuelve una tupla con la media y el estado.
    """


    # Creo una lista vacía. La cual convertiré en tupla tras obtener los resultados
    lista_resultados = []


    # Calculo la media:

    # Creo la variable suma
    suma = 0

    # Recorro la lista de números para sumarlos en la variable suma
    for numero in pLista_Numeros:
        suma += numero

    media = suma / len(pLista_Numeros)


    # Determinar si la media es mayor o igual que nota_aprobado:

    estado = ""

    # Si la media es mayor o igual que nota_aprobado . . .
    if media >= nota_aprobado:

        # . . . el estado será "aprobado" . . .
        estado = "aprobado"
    else:
        # . . . de lo contrario, "suspenso"
        estado = "suspenso"


    # Añado los resultados a la lista
    lista_resultados.extend([media, estado])

    # Convierto la lista en tupla
    tupla_resultados = tuple(lista_resultados)

    # Devuelvo la tupla con la media y el estado
    return tupla_resultados



# PRUEBAS:

notas_1 = [6, 7, 8, 5, 9]
print(calcular_media_y_estado(notas_1))
# Resultado esperado: (7.0, 'aprobado')

notas_2 = [3, 4, 2, 5, 4]
print(calcular_media_y_estado(notas_2))
# Resultado esperado: (3.6, 'suspenso')

notas_3 = [6, 7, 6, 8]
print(calcular_media_y_estado(notas_3, 7))
# Resultado esperado: (6.75, 'suspenso')

notas_4 = [5, 5, 5]
print(calcular_media_y_estado(notas_4))
# Resultado esperado: (5.0, 'aprobado')









