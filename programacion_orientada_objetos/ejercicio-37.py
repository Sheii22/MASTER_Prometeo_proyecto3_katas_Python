"""
Ejercicio 37:

Genera un programa que nos indique si es de noche, de día o de tarde
según la hora proporcionada por el usuario.
"""
from datetime import datetime

# En Python, para trabajar con horas y tiempos se utiliza la librería estándar datetime.
# Dentro del módulo "datetime", existen varias clases y métodos específicos
# para trabajar con la hora.

# try(teoría): encierra la operación propensa a fallos o código riesgoso
try:

    # Solicitar la hora al usuario, en formato HH:MM
    hora_usuario = input("¿Qué hora es? (formato HH:MM, ejemplo: 14:30): ")

    # Convierto la cadena de texto a objeto datetime
    # (strptime valida automáticamente horas y minutos)
    objeto_hora = datetime.strptime(hora_usuario, "%H:%M")

    # Extraigo solo el número entero de la hora (0 a 23)
    hora = objeto_hora.hour


    # Evaluación de los períodos del día:

    # Es de día
    if 6 <= hora < 12:
        print("Es de día")

    # Es de tarde
    elif 12 <= hora < 20:
        print("Es de tarde")

    # Es de noche
    else: # (20 <= hora <= 23) or (0 <= hora < 6):
        print("Es de noche")

    """
    Aclaraciones: Como datetime.strptime() ya valida que la hora introducida esté en el rango 
    de "0" a "23"(lanzando "ValueError" si colocan algo fuera de rango como `"25:00"`), 
    no hace falta una tercera condición explícita.
    """


# MANEJO DE EXCEPCIONES:
# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.
# MANEJO DEL ERROR: capturamos la excepción al llamar a la función.
except ValueError as error:
    print(f"ERROR. La hora indicada no es válida (usa el formato HH:MM). {error}")