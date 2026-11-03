"""
Ejercicio 34:

Crea la clase Arbol
  + Define un árbol genérico con un tronco y ramas como atributos.
  + Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
  + Código a seguir:
        a. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
        b. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
        c. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista
           de ramas.
        d. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas
           las ramas existentes.
        e. Implementar el método quitar_rama para eliminar una rama en una posición específica.
        f. Implementar el método info_arbol para devolver información sobre la longitud del tronco,
           el número de ramas y sus longitudes.
  + Caso de uso:
        a. Crear un árbol.
        b. Hacer crecer el tronco una unidad.
        c. Añadir una nueva rama.
        d. Hacer crecer todas las ramas una unidad.
        e. Añadir dos nuevas ramas.
        f. Retirar la rama situada en la posición 2.
        g. Obtener información sobre el árbol.
"""


# OBJETO Arbol = Crea la clase Arbol:
class Arbol:
    """
    Clase que representa un árbol genérico con tronco y ramas.
    """

    # ATRIBUTOS: características del objeto: tronco y ramas (obj Arbol)
    # MÉTODOS: funciones definidas dentro de una clase,
    #          que representan las acciones que realiza el objeto.



    # METODO CONSTRUCTOR = árbol genérico:
    # Define un árbol genérico con un tronco y ramas como atributos.
    # a. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    def __init__(self):
        """
        Método constructor: Inicializa un árbol con un tronco de longitud 1
        y una lista vacía de ramas.
        """
        self.tronco = 1
        self.ramas = []


    # PRIMER MÉTODO: - crecer_tronco -
    def crecer_tronco(self):
        """
        Método para aumentar la longitud del tronco en una unidad.
        """
        self.tronco += 1  # self.tronco = self.tronco + 1


    # SEGUNDO MÉTODO: - nueva_rama -
    def nueva_rama(self):
        """
        Método para agregar una nueva rama de longitud 1 a la lista de ramas.
        """
        self.ramas.append(1)


    # TERCER MÉTODO: - crecer_ramas -
    def crecer_ramas(self):
        """
        Método para aumentar en una unidad la longitud de todas las ramas existentes.
        """
                       # List Comprehension
        self.ramas = [ rama + 1 for rama in self.ramas]
        # Recorro la lista de ramas(self.ramas) mediante un bucle for
        # y por cada rama, aplico: "rama + 1". Es decir, aumento en una unidad
        # la longitud de cada rama.


    # CUARTO MÉTODO: - quitar_rama -
    def quitar_rama(self, posicion):
        """
        Método para eliminar una rama en una posición específica(índice).
        :param posicion(int): Índice de la rama a eliminar.
        :return: devuelve la rama eliminada o un mensaje si el índice/posición
        pasada por parámetro no existe.
        """
        # Me aseguro de que la posicion o índice está dentro del rango posible:
        if 0 <= posicion < len(self.ramas):
            return self.ramas.pop(posicion)
        else:
            print(f"ERROR. La {posicion} indicada no existe en la lista de ramas.")


    # QUINTO MÉTODO: - info_arbol -
    def info_arbol(self):
        """
        Método para devolver información sobre la longitud del tronco,
        el número de ramas y sus longitudes.
        """
        return (f"Información del árbol: \n"
                f"Longitud del tronco = {self.tronco} \n"
                f"Número de ramas = {len(self.ramas)} \n"
                f"Longitud de cada rama = {self.ramas}")

        # Nota: "\n": para saltar a la siguiente línea dentro de una cadena de texto.



# PRUEBAS - Caso de uso:


#  a. Crear un árbol.
arbol = Arbol()

#  b. Hacer crecer el tronco una unidad.
arbol.crecer_tronco()

#  c. Añadir una nueva rama.
arbol.nueva_rama()

#  d. Hacer crecer todas las ramas una unidad.
arbol.crecer_ramas()

#  e. Añadir dos nuevas ramas.
arbol.nueva_rama()
arbol.nueva_rama()

#  f. Retirar la rama situada en la posición 2.
arbol.quitar_rama(2)

#  g. Obtener información sobre el árbol.
print(arbol.info_arbol())
    # Nota para mi: como el método "info_arbol()" hace un return de la cadena de texto
    #  con la información (en lugar de hacer un print() interno),
    #  si llamo solo a "arbol.info_arbol()", Python devolverá el texto pero
    #  no lo mostrará por la pantalla/consola. Por eso, para imprimirlo por pantalla
    #  envuelvo la llamada al método en un "print()"


