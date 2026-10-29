"""
Ejercicio 32:

Crea una función que tome un nombre completo y una lista de empleados,
busque el nombre en la lista y devuelva el puesto del empleado si se encuentra;
de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
"""

def buscar_puesto_empleado(pNombre_completo, pLista_empleados):
    """
    Esta función, dados un nombre completo y una lista de empleados,
    busca el nombre en la lista y devuelve el puesto del empleado si se encuentra;
    de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

    Args:
        pNombre_completo (str): una cadena de caracteres.
        pLista_empleados (List[dict]): lista con información de empleados.

    Returns:
        str: devuelve el puesto del empleado si se encuentra; de lo contrario,
        devuelve un mensaje indicando que la persona no trabaja aquí.
    """


    # 1. Normalizar el nombre buscado (sin espacios a los lados y minúsculas)
    nombre_buscado_limpio = pNombre_completo.strip().lower()


    # 2. Recorrer la lista de empleados diccionario a diccionario
    for empleado in pLista_empleados:

        # Extraer el nombre del empleado actual y normalizarlo
        nombre_empleado = empleado.get("nombre", "").strip().lower()
            # Para que el programa no se rompa:
            # empleado.get("nombre", "") = empleado.get("clave", valor_por_defecto):
            # valor_por_defecto = "" : Si la clave `"nombre"` NO existe en el diccionario,
            # en lugar de devolver `None` o lanzar un error de tipo `KeyError`,
            # devuelve la cadena vacía ""


        # Comprobar si coincide con el nombre buscado
        if nombre_buscado_limpio == nombre_empleado:

            puesto = empleado.get("puesto", "Puesto no especificado")
            # El texto "Puesto no especificado" cumple la función
            # de valor predeterminado o de respaldo (fallback). Es decir,
            # Si el diccionario NO contiene la clave "puesto":
            # en lugar de interrumpir el programa con un error de tipo "KeyError"
            # o devolver "None", ".get()" asigna automáticamente
            # la cadena "Puesto no especificado"

            return f"El puesto de {pNombre_completo} es: {puesto}"


    # 3. Si el bucle termina sin encontrar coincidencias
    return f"{pNombre_completo} no trabaja aquí."



# PRUEBAS:


# Lista de empleados de prueba (lista de diccionarios):
empleados = [
    {"nombre": "Ana Pérez", "puesto": "Desarrolladora Python"},
    {"nombre": "Carlos Gómez", "puesto": "Analista de Datos"},
    {"nombre": "Laura Martínez", "puesto": "Directora de Proyectos"},
]


print("Prueba 1:", buscar_puesto_empleado("Carlos Gómez", empleados))
# Output: El puesto de Carlos Gómez es: Analista de Datos

print("Prueba 2:", buscar_puesto_empleado(" ana pérez ", empleados))
# Output: El puesto de ana pérez es: Desarrolladora Python

print("Prueba 3:", buscar_puesto_empleado("Pedro Rodríguez", empleados))
# Output: Pedro Rodríguez no trabaja aquí.