"""
Ejercicio 30:

Crea una función que determine si dos palabras son anagramas, es decir,
si están formadas por las mismas letras pero en diferente orden.
"""

def anagramas(pPalabra_1, pPalabra_2):
    """
    Esta función booleana determina si dos palabras son anagramas.

    Args:
        pPalabra_1 (str): una palabra.
        pPalabra_2 (str): otra palabra.

    Returns:
        bool: devuelve true si las palabras son anagramas y false en caso contrario.
    """


    # 1. Evitar falsos negativos por diferencias de formato:

    # Convertir las cadenas a minúsculas(para no diferenciar misma letra en mayúscula y minúscula):
    palabra_1 = pPalabra_1.lower()
    palabra_2 = pPalabra_2.lower()

    # Eliminar espacios intermedios:
    palabra_1 = palabra_1.replace(" ", "")
    palabra_2 = palabra_2.replace(" ", "")
        # Notas: reasigno las variables porque sino el valor de las variables no se modifica.
        # Sintaxis del método de string:
        #  "replace()": replace(old/reemplazado, new/por lo que se va a reemplazar)



    # ¿Son anagrama?


    # 2. Si  NO tienen la misma longitud, NO son anagrama(verificar la longitud)
    if len(palabra_1) != len(palabra_2):
        return False


    # 3. Ordenar los caracteres alfabéticamente

    # Método de listas: sorted(iterable) - Devuelve una nueva lista ORDENADA
    #                                      (no altera la lista original)
    # Si las dos palabras NO comparten exactamente las mismas letras, NO son anagrama
    if sorted(palabra_1) != sorted(palabra_2):
        return False


    # SON ANAGRAMA(si han llegado hasta aquí y por tanto han pasado todas las condiciones)
    return True



# PRUEBAS:

print("Prueba 1 ('roma' y 'amor'):", anagramas("roma", "amor"))
# Output: True

print("Prueba 2 ('Listen' y 'Silent'):", anagramas("Listen", "Silent"))
# Output: True

print("Prueba 3 ('casa' y 'saco'):", anagramas("casa", "saco"))
# Output: False

print("Prueba 4 ('i am lord voldemort' y 'tom marvolo riddle'):", anagramas("i am lord voldemort", "tom marvolo riddle"))
# Output: True