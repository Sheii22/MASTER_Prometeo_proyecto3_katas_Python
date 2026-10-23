"""
Ejercicio 11:

Escribe un programa que pida al usuario que introduzca su edad.
Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
(por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
"""


# try(teoría): encierra la operación propensa a fallos o código riesgoso
try:
    # Pedir al usuario que introduzca su edad
    edad_usuario = int(input("Indica tu edad: "))
                   # Transformar la entrada de texto en números mediante "int()"

    # Validación de rango: si está fuera de 0 - 120, lanzo ValueError
    if edad_usuario < 0 or edad_usuario > 120:
        raise ValueError("La edad ingresada está fuera del rango permitido (0 - 120).")


# MANEJO DE EXCEPCIONES:

# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.

# EXCEPCIÓN: valor no numérico o valor fuera del rango esperado(ValueError):
except ValueError:

    # Capturamos el error
    print("ERROR. El valor tiene que ser un numérico o estar dentro del rango: 0-120 ")

# else(teoría): se ejecuta ÚNICAMENTE si NO ocurrió ninguna excepción dentro del bloque "try".
else:

    print(f"¡Operación exitosa! Tu edad es: {edad_usuario}")

# finally(teoría): se ejecuta SIEMPRE obligatoriamente(haya o no error)
finally:

    print("Fin del programa")



