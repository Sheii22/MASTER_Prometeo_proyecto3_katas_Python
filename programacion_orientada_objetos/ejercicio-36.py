"""
Ejercicio 36:

Crea una función llamada procesar_texto
   + Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras
     o eliminar_palabra.
   + Código a seguir:
        a. Crear una función contar_palabras que cuente el número de veces
           que aparece cada palabra en el texto y devuelva un diccionario.
        b. Crear una función reemplazar_palabras para sustituir una palabra_original
           por una palabra_nueva en el texto y devolver el texto modificado.
        c. Crear una función eliminar_palabra que elimine una palabra del texto
           y devuelva el texto sin ella.
        d. Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar",
           "eliminar") y un número variable de argumentos según la opción elegida.
   + Caso de uso:
        Verificar el funcionamiento completo de procesar_texto.
"""

# a.
def contar_palabras(pTxt):
    """
    Función que cuenta el número de veces que aparece cada palabra en el texto
    y devuelve un diccionario.
    """

    # Creo un diccionario vacío, el cual retornaré
    frecuencia_palabras = dict()

    # Separo las palabras en una lista de palabras
    lista_palabras = pTxt.lower().split()
                        # Separar por espacios: ".split()": (sin pasarle argumentos)
                        # dividirá el texto tomando cualquier espacio en blanco como separador
                        # y devolverá una lista con cada palabra limpia

                        # ".lower()" = Convierto el texto a minúsculas para que al buscar
                        # una palabra específica, no me diferencie entre mayúsculas y minúsculas

    # Recorro la lista de palabras para contar el número de veces que aparece cada una
    for palabra in lista_palabras:

        # Obtener el número de apariciones de cada palabra: método count()
        # Sintaxis: secuencia.count(elemento)
        numero_apariciones = lista_palabras.count(palabra.lower())

        # Si la palabra ha sido encontrada ...
        if numero_apariciones != 0:
            # ... la añado al diccionario
            frecuencia_palabras[palabra] = numero_apariciones


    return frecuencia_palabras


# PRUEBAS:

print("--- PRUEBAS función ´contar_palabras()´ ---")

texto1 = "Python es genial y Python es fácil"
print(f"PRUEBA 1: {contar_palabras(texto1)}")
# Resultado: {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'fácil': 1}

texto2 = "Hola hola HOLA Mundo mundo"
print(f"PRUEBA 2: {contar_palabras(texto2)}")
# Resultado: {'hola': 3, 'mundo': 2}

texto3 = "El sol brilla en el solado"
print(f"PRUEBA 3: {contar_palabras(texto3)}")
# Resultado: {'el': 2, 'sol': 1, 'brilla': 1, 'en': 1, 'solado': 1}

texto4 = "Python"
print(f"PRUEBA 4: {contar_palabras(texto4)}")
# Resultado: {'python': 1}

texto5 = ""
print(f"PRUEBA 5: {contar_palabras(texto5)}")
# Resultado: {}


# b.
def reemplazar_palabras(palabra_original, palabra_nueva, pTxt):
    """
    Función para sustituir una palabra_original por una palabra_nueva en el texto
    y devolver el texto modificado.
    """

    # TO DO
    # Separo las palabras en una lista de palabras
    lista_palabras = pTxt.split()

# PRUEBAS:

print("--- PRUEBAS función ´reemplazar_palabras()´ ---")


# c.
def eliminar_palabra(palabra, pTxt):
    """
    Función que elimina una palabra del texto y devuelve el texto sin ella.
    """

    # TO DO
    # Separo las palabras en una lista de palabras
    lista_palabras = pTxt.split()

# PRUEBAS:

print("--- PRUEBAS función ´eliminar_palabra()´ ---")


# d.
def procesar_texto(pTxt, pOpcion_especificada):
    """
    Esta función procesa un texto según la opción especificada: contar_palabras,
    reemplazar_palabras o eliminar_palabra.

    Args:
        pTxt (str): un texto.
        pOpcion_especificada: una función.

    Returns:
        dict | txt | : devuelve el resultado de la opción especificada(función) .
    """
    # TO DO



# PRUEBAS - Caso de uso:


#  Verificar el funcionamiento completo de procesar_texto.

print("--- PRUEBAS función ´procesar_texto(pTxt, pOpcion_especificada)´ ---")