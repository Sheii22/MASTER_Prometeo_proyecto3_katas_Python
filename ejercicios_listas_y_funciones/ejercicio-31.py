"""
Ejercicio 31:

Crea una función que solicite al usuario ingresar una lista de nombres
y luego un nombre para buscar en esa lista. Si el nombre está en la lista,
imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción..
"""

"""
LANZAR UNA EXCEPCIÓN PERSONALIZADA:

Se define una nueva clase que hereda de la clase base Exception(o de una de sus subclases) 
y se utiliza la palabra clave raise para lanzarla intencionalmente 
cuando no se cumple una condición dentro del flujo del programa.
"""

# 1. DEFINICIÓN DE LA EXCEPCIÓN PERSONALIZADA
class NombreNoEncontradoError(Exception):
    """
    Excepción personalizada
    que se lanza cuando el nombre no está en la lista.
    """
    pass


def buscar_nombre():
    """
    Esta función solicita al usuario una lista de nombres y un nombre a buscar.
    Imprime un mensaje si lo encuentra o lanza NombreNoEncontradoError si no existe.
    """


    # Solicitar al usuario una lista de nombres:
    pLista_nombres = input("Ingrese una lista de nombres(separados por comas y espacios): ")
                    # "input()" devuelve siempre un único texto (str)
                    # Lo cual puede causar errores para este caso:
                    # Si por ejemplo, busco un nombre sobre un str,
                    # Python buscará subcadenas (por ejemplo, `"Ana"` dentro de `"Anabel"`
                    # daría `True`).
                    # Solución: convertir el input() en una lista real con .split(",")
    # Para transformar el texto en una lista de cadenas independientes eliminando espacios extras.
    pLista_real_nombres = [nombre.strip() for nombre in pLista_nombres.split(",")]


    # Solicitar al usuario un nombre:
    pNombre = input("Ingrese un nombre: ").strip()
        # Aplicar strip() para limpiar automáticamente cualquier espacio accidental
        # antes o después del texto



    # Si el nombre está en la lista ...
    if pNombre in pLista_real_nombres:

        # ... imprimo un mensaje indicando que fue encontrado;
        print(f"El nombre {pNombre} fué encontrado en la lista: {pLista_real_nombres}")

    # de lo contrario, ...
    else:
        # ... lanza una excepción personalizada..
        raise NombreNoEncontradoError("¡ERROR! El nombre no está en la lista de palabras")



# try(teoría): encierra la operación propensa a fallos o código riesgoso
try:

    # PRUEBAS:

    buscar_nombre()

    """
    Prueba 1:
    
    Ingrese una lista de nombres(separados por comas y espacios): Patxi, Ainhoa, Maria, Laura
    Ingrese un nombre: Ainhoa
    El nombre Ainhoa fué encontrado en la lista: ['Patxi', 'Ainhoa', 'Maria', 'Laura']
    ¡Operación exitosa! NO ocurrió ninguna excepción(error)
    Fin del programa
    """

    """
    Prueba 2:
    
    Ingrese una lista de nombres(separados por comas y espacios): Anabel, Rosa, José, Jesús, Ander
    Ingrese un nombre: Ana
    Captura controlada del error: ¡ERROR! El nombre no está en la lista de palabras
    Fin del programa
    """



# MANEJO DE EXCEPCIONES:
# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.

# MANEJO DEL ERROR: capturamos la excepción al llamar a la función
except NombreNoEncontradoError as error:

    print(f"Captura controlada del error: {error}")



# else(teoría): se ejecuta ÚNICAMENTE si NO ocurrió ninguna excepción dentro del bloque "try".
else:

   print("¡Operación exitosa! NO ocurrió ninguna excepción(error)")



# finally(teoría): se ejecuta SIEMPRE obligatoriamente(haya o no error)
finally:

    print("Fin del programa")