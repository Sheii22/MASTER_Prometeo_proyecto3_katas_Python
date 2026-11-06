"""
Ejercicio 39:

Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo",
"circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área
de la figura).
"""

# Para poder utilizar la constante que proporciona el número π (pi). Dentro del módulo math.
import math

def calcular_area_figura(pFigura, pDatos):
    """
    Esta función calcula el área de una figura.

    Args:
        pFigura (str): una cadena que puede ser "rectangulo", "circulo" o "triangulo".
        pDatos (tuple( int | float )): una tupla con los datos necesarios para calcular el área de la figura.

    Returns:
        float : devuelve el área de la figura.
    """


    # Convierto el parámetro "pFigura" a minúsculas
    # para evitar problemas con mayúsculas/minúsculas
    pFigura = pFigura.lower().strip()
                     # ".lower()": convierte todos los caracteres de la cadena a minúsculas.
                     # ".strip()": elimina los espacios en blanco(u otros caracteres)
                     # tanto al inicio como al final de la cadena


    # Creo condicionales para calcular el área de las diferentes figuras
    # y lanzo un error si la figura no es la esperada
    if pFigura == "rectangulo":
        # area_rectangulo = base * altura
        # pDatos = (base, altura)

        # Comprobación previa
        if len(pDatos) != 2:
            raise ValueError("Para el rectángulo se requieren 2 datos: (base, altura).")

        # Extraigo los datos de la tupla(pDatos) y los convierto en float(número decimal)
        base = float(pDatos[0])
        altura = float(pDatos[1])

        # Calculo el área del rectángulo
        area_rectangulo = base * altura

        return area_rectangulo

    elif pFigura == "circulo":
        # area_circulo = π * radio^2
        # pDatos = (radio,)

        # Comprobación previa
        if len(pDatos) != 1:
            raise ValueError("Para el círculo se requiere 1 dato: (radio,).")

        # Python tiene una constante que proporciona el número π (pi) - En el módulo math
        numero_pi = math.pi
        radio = float(pDatos[0])

        # Calculo el área del círculo
        area_circulo = numero_pi * radio**2

        return area_circulo

    elif pFigura == "triangulo":
        # area_triangulo = (base * altura) / 2
        # pDatos = (base, altura)

        # Comprobación previa
        if len(pDatos) != 2:
            raise ValueError("Para el triángulo se requieren 2 datos: (base, altura).")

        # Extraigo los datos de la tupla(pDatos) y los convierto en float(número decimal)
        base = float(pDatos[0])
        altura = float(pDatos[1])

        # Calculo el área del triangulo
        area_triangulo = (base * altura)/2

        return area_triangulo

    else: # ERROR
        # Lanzo una excepción si la opción pasada por parámetro no es válida
        raise ValueError("Debe elegir de qué figura quiere calcular el área: `rectangulo`,`circulo` o `triangulo`")



# PRUEBAS:


# a. Probar opción 'rectangulo' (base=5, altura=4) -> 5 * 4 = 20.0
resultado_rectangulo = calcular_area_figura("rectangulo", (5, 4))
print(f"a) Rectángulo (base=5, altura=4):\n {resultado_rectangulo}\n")
# Output/Resultado: 20.0


# b. Probar opción 'circulo' (radio=3) -> π * 3^2 ≈ 28.27
# Nota: La tupla de un solo elemento requiere la coma final: (3,)
resultado_circulo = calcular_area_figura("circulo", (3,))
print(f"b) Círculo (radio=3):\n {resultado_circulo:.2f}\n")
# Output/Resultado: 28.27

"""
Notas/aclaraciones:  
    "resultado_circulo:.2f" -> dentro de un f-string es un formato de Python 
                               para controlar cuántos decimales se muestran 
                               de un número flotante (`float`).
                               
                               Desglose paso a paso:
                               1. "resultado_circulo": Es la variable que contiene 
                                                       el número decimal.
                               2. " : "(dos puntos): Le indica a Python que a continuación 
                                                  vienen las instrucciones de formato.
                               3. " .2 ": Especifica la cantidad exacta de dígitos decimales 
                                          que deseas mostrar (en este caso, 2 decimales).
                               4. " f ": Indica que el valor original es de tipo float
                                         (número flotante/decimal)
"""


# c. Probar opción 'triangulo' (base=6, altura=3) -> (6 * 3) / 2 = 9.0
resultado_triangulo = calcular_area_figura("triangulo", (6, 3))
print(f"c) Triángulo (base=6, altura=3):\n {resultado_triangulo}\n")
# Output/Resultado: 9.0


# d. Probar tolerancia a mayúsculas ('RECTANGULO')
resultado_mayusculas = calcular_area_figura("RECTANGULO", (10, 2))
print(f"d) 'RECTANGULO' (base=10, altura=2):\n {resultado_mayusculas}\n")
# Output/Resultado: 20.0


# e. Probar control de excepciones: figura no válida ('pentagono')
try:  # try(teoría): encierra la operación propensa a fallos o código riesgoso
    calcular_area_figura("pentagono", (5, 5))

# MANEJO DE EXCEPCIONES:

# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.
except ValueError as error:
    print(f"e) Captura de excepción (figura no válida):\n {error}\n")
# Output/Resultado: Debe elegir de qué figura quiere calcular el área:
# `rectangulo`, `circulo` o `triangulo`



# f. Probar control de excepciones: datos insuficientes en la tupla
try:
    calcular_area_figura("triangulo", (5,))

except ValueError as error:
    print(f"f) Captura de excepción (datos insuficientes):\n {error}\n")
# Output/Resultado: Para el triángulo se requieren 2 datos: (base, altura).


