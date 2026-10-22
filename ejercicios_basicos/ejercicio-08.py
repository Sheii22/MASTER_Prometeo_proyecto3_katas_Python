"""
Ejercicio 8:

Escribe un programa que pida al usuario dos números e intente dividirlos.
Si el usuario ingresa un valor no numérico o intenta dividir por cero,
maneja esas excepciones de manera adecuada y muestra un mensaje
indicando si la división fue exitosa o no.
"""

# try(teoría): encierra la operación propensa a fallos o código riesgoso
# try: pide al usuario dos números e intente dividirlos
try:

    """
    Interactuar con el usuario: pedir al usuario dos números

    (Capturar datos introducidos por el usuario mediante input()
    permite tomar un valor de entrada por parte del usuario
    desde la línea de comandos o terminal.
    Devuelve una cadena de caracteres(str).)
    """

    # Transformar la entrada de texto en números mediante "int()"
    pNum_1 = int(input("Introduce un número: "))
    pNum_2 = int(input("Introduce otro número: "))

    resultado_division = pNum_1 / pNum_2

    print(f"El resultado de la división es: {resultado_division}")

# MANEJO DE EXCEPCIONES:

# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.

# EXCEPCIÓN: valor no numérico(ValueError):
# el usuario introduce texto cuando se esperaba un número
except ValueError:

    # Capturamos el error si el usuario ingresa texto no numérico
    print("La división NO fue exitosa, porque uno o ambos valores introducidos no son válidos")

# EXCEPCIÓN: dividir entre cero(ZeroDivisionError)
except ZeroDivisionError:

    # Capturamos el error
    print("La división NO fue exitosa, porque no es posible dividir entre cero.")

# else(teoría): se ejecuta ÚNICAMENTE si NO ocurrió ninguna excepción dentro del bloque "try".
# finally(teoría): se ejecuta SIEMPRE obligatoriamente(haya o no error)

# Enunciado: "... muestra un mensaje indicando si la división fue exi9tosa o no."
else:

    print("La división fue exitosa")
