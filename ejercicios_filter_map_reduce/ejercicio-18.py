"""
Ejercicio 18:

Escribe un programa en Python que cree una lista de diccionarios
con información de estudiantes (nombre, edad, calificación)
y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.
"""


# 1. Crear la lista de estudiantes(dicionarios con información
#    de estudiantes (nombre, edad, calificación) a partir de generar
#    estudiantes aleatorios(random):

import random

def generar_estudiantes_aleatorios(pCantidad):
    """
    Genera una lista de diccionarios con información aleatoria de estudiantes.
    """
    # Lista base de nombres para elegir al azar
    nombres_base = ["Ana", "Carlos", "Beatriz", "David", "Elena", "Fernando", "Gloria",
                    "Hugo", "Isabel", "Javier"]

    # Creo la lista de dicionarios con información de los estudiantes
    # usando list comprehension
    lista_estudiantes = [
        { "nombre": random.choice(nombres_base),
                  # random.choice(lista): Selecciona un elemento al azar de una lista
                  # (para los nombres).

          # Edad entre 18 y 26 años:
          "edad": random.randint(18, 26),
                # random.randint(a, b): devuelve un número entero aleatorio
                # entre "a" y "b" (ambos inclusive)
                # (para edades y calificaciones).

          # Nota entre 0 y 100
          "calificacion": random.randint(0, 100)  }

         # list comprehension:
         # Explicación: "Repite una acción un número exacto de veces(pCantidad),
         #               sin importar el valor o número del ciclo actual".
         # "range(pCantidad)": genera una secuencia numérica desde "0" hasta "pCantidad - 1"
         # Bucle: "for ... in ...": recorre cada uno de los elementos de la secuencia
         #                          generada por "range()"
         # Guion bajo (_) como variable: hace referencia al nombre de
         #                               una variable de iteración desechable o de "descarte".
         for _ in range(pCantidad) ]

    return lista_estudiantes


# 2. Extraer a los estudiantes con una calificación mayor o igual a 90.

# Genero 20 estudiantes aleatorios:
estudiantes = generar_estudiantes_aleatorios(20)

# Filtramos los sobresalientes(>= 90):
sobresalientes = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))
                 # Recorre la lista "estudiantes", comprueba quién tiene una nota de 90 o superior
                 # y guarda los diccionarios seleccionados en la lista "sobresalientes"


print(f"Número de estudiantes: {len(estudiantes)}")
print(f"Cantidad de sobresalientes (>= 90): {len(sobresalientes)}")

# Estudiantes con una calificación mayor o igual a 90:
print(f"Estudiantes con sobresaliente: {sobresalientes}")


"""
Output:
Número de estudiantes: 20
Cantidad de sobresalientes (>= 90): 4
Estudiantes con sobresaliente: [
               {'nombre': 'Ana', 'edad': 25, 'calificacion': 92}, 
               {'nombre': 'Elena', 'edad': 20, 'calificacion': 99}, 
               {'nombre': 'Isabel', 'edad': 25, 'calificacion': 100}, 
               {'nombre': 'Hugo', 'edad': 26, 'calificacion': 96}]
"""


