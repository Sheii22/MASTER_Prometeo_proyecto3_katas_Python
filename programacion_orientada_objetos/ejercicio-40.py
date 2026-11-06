"""
Ejercicio 40:

Escribe un programa en Python que utilice condicionales para determinar el monto final de
una compra en una tienda en línea, después de aplicar un descuento.

El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido
      (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
"""

# Nota: el programa tiene en cuenta si el descuento es introducido en porcentaje o en euros

# Determinar el monto final de una compra en una tienda en línea:

try:  # try(teoría): encierra la operación propensa a fallos o código riesgoso

    # a. Solicitar al usuario el precio original de un artículo.
    precio_original_articulo = float( input("Indique el precio original del artículo:") )
                               # Convertir la entrada a float para soportar valores decimales

    if precio_original_articulo <= 0:
        raise ValueError("El precio original del artículo debe ser mayor a cero.")

    # b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    cupon_de_descuento = input("Indique si dispone de algún descuento(respuesta sí o no):")

    # c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    if cupon_de_descuento.lower().strip() in ["sí", "si"]: # sí con acento y sin acento
                        # ".lower()": convierte todos los caracteres de la cadena a minúsculas.
                        # ".strip()": elimina los espacios en blanco(u otros caracteres)
                        # tanto al inicio como al final de la cadena

        # PREGUNTAR EL TIPO DE CUPÓN (1: Porcentaje %, 2: Fijo en €)
        print("\n¿Qué tipo de cupón desea aplicar?")
        print(" 1. Porcentaje (%)")
        print(" 2. Importe fijo (€)")
        tipo_cupon = input("Seleccione una opción (1 o 2): ").strip()

        # -- Evaluación según el tipo de cupón elegido --

        # --- OPCIÓN 1: DESCUENTO EN PORCENTAJE (%) ---
        if tipo_cupon in ["1", "porcentaje", "%"]:

            # solicitar el valor del cupón de descuento.
            valor_cupon_de_descuento = float( input("Indique el valor del cupón de descuento:"))

            # d. Aplicar el descuento al precio original, siempre que el valor del cupón
            # sea válido(mayor a cero y menor a 100).

            # Si el valor no es válido
            if (valor_cupon_de_descuento <= 0) or (valor_cupon_de_descuento > 100):

                # Lanzo una excepción
                raise ValueError("El valor del cupón debe ser mayor a cero y menor o igual a 100")

            # Si el valor del cupón es válido ...
            else:
                # ... aplico el descuento al precio original - Calcular el precio final:

                # 1. Calcular porcentaje a pagar:
                porcentaje_a_pagar = 100 - valor_cupon_de_descuento

                # 2. Convertir ese porcentaje restante a decimal:
                decimal_a_pagar = porcentaje_a_pagar / 100

                # 3. Multiplicar el precio original por ese decimal
                # (El resultado será el precio final con el descuento aplicado):
                precio_final = precio_original_articulo * decimal_a_pagar

                # e. Mostrar el precio final de la compra, considerando o no el descuento.
                print(f"El precio final de la compra es: {precio_final:.2f}€")
                                   # " .2f ": dentro de un f-string es un formato de Python
                                   #          para controlar cuántos decimales se muestran
                                   #          de un número flotante (`float`). En este caso,
                                   #          2 decimales.

        # --- OPCIÓN 2: DESCUENTO EN IMPORTE FIJO (€) ---
        elif tipo_cupon in ["2", "fijo", "euros", "€"]:

            # solicitar el valor del cupón de descuento.
            valor_cupon = float(input("Indique el valor del cupón (€):"))

            # d. Aplicar el descuento al precio original, siempre que el valor del cupón
            # sea válido(mayor a cero).

            # Validación del importe fijo
            if valor_cupon <= 0:
                raise ValueError("El valor del cupón en euros debe ser mayor a cero.")

            elif valor_cupon > precio_original_articulo:
                raise ValueError("El descuento no puede ser superior al precio del artículo.")

            # Si el valor del cupón es válido - Calcular el precio final:
            else:

                precio_final = precio_original_articulo - valor_cupon

                # e. Mostrar el precio final de la compra, considerando o no el descuento.
                print(f"El precio final de la compra es: {precio_final:.2f}€")

        else:
            raise ValueError("Tipo de cupón no válido (debe seleccionar 1 o 2).")


    # El usuario NO TIENE un cupón de descuento
    elif cupon_de_descuento.lower().strip() in ["no"]:

        precio_final = precio_original_articulo

        # e. Mostrar el precio final de la compra, considerando o no el descuento
        print(f"El precio final de la compra es: {precio_final:.2f} €")

    else:
        raise ValueError("Respuesta no válida para el cupón (debe responder 'sí' o 'no').")


# MANEJO DE EXCEPCIONES:

# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.
except ValueError as error:
    print(f"ERROR. Valor no válido.\n {error}\n")


