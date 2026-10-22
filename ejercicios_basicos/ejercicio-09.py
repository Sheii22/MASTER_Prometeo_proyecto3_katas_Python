"""
Ejercicio 9:

Escribe una función que tome una lista de nombres de mascotas como parámetro
y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
Usa la función filter().
"""

def excluir_mascotas_prohibidas(pNombres_mascotas):
    """
    Esta función, dada una lista de nombres de mascotas,
    devuelve una nueva lista excluyendo ciertas mascotas prohibidas en España.

    Args:
        pNombres_mascotas (list[str]): una lista de nombres de mascotas.

    Returns:
        list[str]: devuelve una nueva lista excluyendo ciertas mascotas prohibidas en España.
    """


    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]


    # Genero una nueva lista con las mascotas que NO aparecen en la lista "mascotas_prohibidas":
    mascotas_permitidas = list(filter(lambda mascota: mascota not in mascotas_prohibidas,
                                      pNombres_mascotas))
        # filter(): Recorre directamente la lista "pNombres_mascotas" sin necesidad de un bucle for
        # filter(función_booleana, iterable)

        # función_booleana = función lambda: "lambda mascota: mascota not in mascotas_prohibidas":
        # Evalua elemento a elemento del iterable pasado por parámetro: "pNombres_mascotas"

        # Para ver la lista: "list( . . . )"

    return mascotas_permitidas



# PRUEBAS:

lista_1 = ["Perro", "Mapache", "Gato", "Tigre", "Hámster", "Cocodrilo"]
print("Prueba 1:", excluir_mascotas_prohibidas(lista_1))
# Resultado esperado: ['Perro', 'Gato', 'Hámster']

lista_2 = ["Perro", "Gato", "Canario", "Pez Dorado"]
print("Prueba 2:", excluir_mascotas_prohibidas(lista_2))
# Resultado esperado: ['Perro', 'Gato', 'Canario', 'Pez Dorado']

lista_3 = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
print("Prueba 3:", excluir_mascotas_prohibidas(lista_3))
# Resultado esperado: []

lista_4 = []
print("Prueba 5:", excluir_mascotas_prohibidas(lista_4))
# Resultado esperado: []

