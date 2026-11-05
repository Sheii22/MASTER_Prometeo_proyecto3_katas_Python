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

print("\n--- PRUEBAS función ´contar_palabras()´ ---")

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

    # El método ".replace()" busca todas las apariciones del texto original ("old")
    # y las reemplaza por el texto nuevo ("new"), devolviendo una nueva cadena de texto
    # con la transformación realizada.
    # Sintaxis: .replace(old, new)
    texto_modificado = pTxt.replace(palabra_original, palabra_nueva)

    return texto_modificado


# PRUEBAS:

print("\n--- PRUEBAS función ´reemplazar_palabras()´ ---")

texto1 = "Hola mundo"
res1 = reemplazar_palabras("mundo", "Python", texto1)
print(f"PRUEBA 1: {res1}")
# Resultado: 'Hola Python'

texto2 = "El perro juega con otro perro"
res2 = reemplazar_palabras("perro", "gato", texto2)
print(f"PRUEBA 2: {res2}")
# Resultado: 'El gato juega con otro gato'

texto3 = "Python es genial y python es fácil"
res3 = reemplazar_palabras("Python", "Java", texto3)
print(f"PRUEBA 3: {res3}")
# Resultado: 'Java es genial y python es fácil'

texto4 = "Aprender Python"
res4 = reemplazar_palabras("C++", "Java", texto4)
print(f"PRUEBA 4: {res4}")
# Resultado: 'Aprender Python'



# c.
def eliminar_palabra(palabra_a_eliminar, pTxt):
    """
    Función que elimina una palabra del texto y devuelve el texto sin ella.
    """

    # 1. Para asegurarme de eliminar únicamente palabras completas e independientes
    # y mantener los espacios perfectos entre palabras,
    # separo el texto en una lista de palabras.
    # Mediante el método de string ".split()":
    lista_palabras = pTxt.split()

    # 2. Filtro la lista conservando solo las palabras distintas a la que deseo eliminar.
    # Para ello, utilizo List comprehension
    # Sintaxis: nombre_lista = [elemento for elemento in iterable if condicion]
    lista_palabras_filtradas = [palabra for palabra in lista_palabras if palabra.lower() != palabra_a_eliminar.lower()]
          # Nota: ".lower()": al hacer la comparación(en el if), convierto el txt en minúsculas para que
          # la búsqueda no sea sensible a mayúsculas

    # 3. Vuelvo a unir la lista filtrada en una sola cadena de texto.
    # Para ello, utilizo el método de string ".join()":
    # Nota: este método utiliza la cadena sobre la que se llama como separador
    resultado_txt = " ".join(lista_palabras_filtradas)

    return resultado_txt


# PRUEBAS:

print("\n--- PRUEBAS función ´eliminar_palabra()´ ---")

texto1 = "El Gato juega con otro gato en el jardín"
res1 = eliminar_palabra("gato", texto1)
print(f"PRUEBA 1: {res1}")
# Resultado: 'El juega con otro en el jardín'

texto2 = "El sol brilla en el solado"
res2 = eliminar_palabra("sol", texto2)
print(f"PRUEBA 2: {res2}")
# Resultado: 'El brilla en el solado'

texto3 = "Python es un lenguaje de programación"
res3 = eliminar_palabra("PYTHON", texto3)
print(f"PRUEBA 3: {res3}")
# Resultado: 'es un lenguaje de programación'

texto4 = "Aprender programación es divertido"
res4 = eliminar_palabra("Java", texto4)
print(f"PRUEBA 4: {res4}")
# Resultado: 'Aprender programación es divertido'



# d.
def procesar_texto(pTxt, pOpcion_especificada, *args):
    """
    Esta función procesa un texto según la opción especificada: contar_palabras,
    reemplazar_palabras o eliminar_palabra.

    Args:
        pTxt (str): un texto.
        pOpcion_especificada: una función.

    Returns:
        dict | txt  : devuelve el resultado de la opción especificada(función).
    """

    # Nota: parámetro : *args: número variable de argumentos según la opción elegida.
    #                          (empaquetado/desempaquetado de argumentos)


    # Procesa un texto según la opción especificada:

    # contar_palabras
    if pOpcion_especificada == "contar":
        return contar_palabras(pTxt)

    # reemplazar_palabras
    elif pOpcion_especificada == "reemplazar":
        return reemplazar_palabras(*args, pTxt)
               # Nota: Al pasar `*args` a `reemplazar_palabras(*args, pTxt)`,
               # Python desempaqueta los argumentos en el orden exacto
               # `(palabra_original, palabra_nueva, pTxt)`.

    # eliminar_palabra
    elif pOpcion_especificada == "eliminar":
        return eliminar_palabra(*args, pTxt)
               # Nota: Para `eliminar_palabra(*args, pTxt)`,
               # se desempaqueta la tupla como `(palabra_a_eliminar, pTxt)`

    # Control de errores: si introducen una opción no válida
    else:
        # Lanzo una excepción si la opción pasada por parámetro no es válida
        raise ValueError("ERROR. No ha seleccionado ninguna opción válida para procesar el texto.")


# PRUEBAS - Caso de uso:

#  Verificar el funcionamiento completo de procesar_texto.

print("\n--- PRUEBAS función ´procesar_texto(pTxt, pOpcion_especificada)´ ---")

texto_ejemplo = "Python es genial y Python es fácil"

# a. Probar la opción "contar"
res_contar = procesar_texto(texto_ejemplo, "contar")
print(f"a) Opción 'contar':\n {res_contar}\n")
# Resultado: a) Opción 'contar':
#  {'python': 2, 'es': 2, 'genial': 1, 'y': 1, 'fácil': 1}

# b. Probar la opción "reemplazar" (pasando 'Python' y 'Java' en *args)
res_reemplazar = procesar_texto(texto_ejemplo, "reemplazar", "Python", "Java")
print(f"b) Opción 'reemplazar':\n {res_reemplazar}\n")
# Resultado: b) Opción 'reemplazar':
#  Java es genial y Java es fácil

# c. Probar la opción "eliminar" (pasando 'genial' en *args)
res_eliminar = procesar_texto(texto_ejemplo, "eliminar", "genial")
print(f"c) Opción 'eliminar':\n {res_eliminar}\n")
# Resultado: c) Opción 'eliminar':
#  Python es y Python es fácil

# d. Probar control de excepciones (opción no válida)
# try(teoría): encierra la operación propensa a fallos o código riesgoso
try:
    procesar_texto(texto_ejemplo, "modificar")

# MANEJO DE EXCEPCIONES:
# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.
# MANEJO DEL ERROR: capturamos la excepción al llamar a la función.
except ValueError as error:
    print(f"d) Captura de excepción:\n {error}")
# Resultado: d) Captura de excepción:
#  ERROR. No ha seleccionado ninguna opción válida para procesar el texto.

