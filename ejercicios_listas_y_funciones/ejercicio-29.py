"""
Ejercicio 29:

Crea una función que convierta una variable en una cadena de texto
y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
"""

def convertir_variable_en_txt(pVariable):
    """
    Esta función convierte una variable en una cadena de texto
    y enmascara todos los caracteres con el carácter '#' excepto los últimos cuatro.

    Args:
        pVariable (Any): una variable (números, cadenas, etc.).

    Returns:
        str: una cadena de texto.
    """


    # 1. Convertir la variable a cadena de texto
    cadena_de_txt = str(pVariable)


    # 2. Enmascarar todos los caracteres con el carácter '#' excepto los últimos cuatro:

    # 2.1. Si tiene 4 caracteres o menos, no se enmascara nada(control de seguridad)
    if len(cadena_de_txt) <= 4:
        return cadena_de_txt

    # 2.2. Enmascarar con slicing:
    cadena_enmascarada = "#" * (len(cadena_de_txt) - 4) + cadena_de_txt[-4: ]
           # '"#" * (len(cadena_de_txt) - 4)':
           # colócame el caracter "#" - ¿Cuántas veces? - La longitud de la cadena de txt - 4
           # Y súmale:
           # slicing de Strings en Python: nombre_variable_str[start: stop] :
           # " cadena_de_txt[-4: ] "
           # start = -4 (índices negativos. Los últimos 4 caracteres)
           # stop =     (al no poner nada, le estoy diciendo que hasta el final)


    return cadena_enmascarada



# PRUEBAS:

val_1 = 1234567890123456
print("Prueba 1 (número largo):", convertir_variable_en_txt(val_1))
# Output: ############3456

val_2 = "miclavesecreta123"
print("Prueba 2 (string largo):", convertir_variable_en_txt(val_2))
# Output: #############a123

val_3 = "1234"
print("Prueba 3 (4 caracteres):", convertir_variable_en_txt(val_3))
# Output: 1234

val_4 = 99
print("Prueba 4 (menos de 4):", convertir_variable_en_txt(val_4))
# Output: 99