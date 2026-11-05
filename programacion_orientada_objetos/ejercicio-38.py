"""
Ejercicio 38:

Escribe un programa que determine qué calificación en texto tiene un alumno según
su calificación numérica.
Reglas:
        0 - 69: insuficiente
        70 - 79: bien
        80 - 89: muy bien
        90 - 100: excelente
"""

# try(teoría): encierra la operación propensa a fallos o código riesgoso
try:

    # Solicitar la calificación al usuario y convertirla a número flotante/decimal.
    # Para prevenir errores
    calificacion_numerica = float( input("Escribe tu calificación:") )


    #  Validar primero que "calificacion_numerica" esté en el rango de 0 a 100
    if calificacion_numerica < 0 or calificacion_numerica > 100:
        raise ValueError("Su calificación numérica debe estar en un rango de 0-100")

    elif calificacion_numerica < 70:
        print("Su calificación es: insuficiente")

    elif calificacion_numerica < 80:
        print("Su calificación es: bien")

    elif calificacion_numerica < 90:
        print("Su calificación es: muy bien")

    else: # 90 <= calificacion_numerica <= 100:
        print("Su calificación es: excelente")



# MANEJO DE EXCEPCIONES:
# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.
except ValueError as error:
    print(f"ERROR: Entrada no válida ({error})")