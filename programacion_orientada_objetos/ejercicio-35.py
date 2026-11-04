"""
Ejercicio 35:

Crea la clase UsuarioBanco:
   + Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
   + Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
   + Código a seguir:
        1. Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
        2. Implementar retirar_dinero para sustraer dinero del saldo,
           lanzando un error si no es posible.
        3. Implementar transferir_dinero para transferir dinero desde otro usuario,
           lanzando un error en caso de fallo.
        4. Implementar agregar_dinero para aumentar el saldo del usuario.
   + Caso de uso:
        a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50,
           ambos con cuenta corriente.
        b. Agregar 20 unidades al saldo de Bob.
        c. Transferir 80 unidades de Bob a Alicia.
        d. Retirar 50 unidades del saldo de Alicia.
"""


# OBJETO UsuarioBanco = Crea la clase UsuarioBanco:
class UsuarioBanco:
    """
    Clase que representa un usuario del banco.
    """

    # ATRIBUTOS: características del objeto: nombre, saldo y cuenta corriente
    # MÉTODOS: funciones definidas dentro de una clase, que representan las acciones
    # que realiza el objeto: retirar_dinero, transferir_dinero, agregar_dinero.



    # METODO CONSTRUCTOR:
    # Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Método constructor: Representa a un usuario de un banco
        con su nombre, saldo y si tiene o no cuenta corriente.
        """

        # Asignación de parámetros a atributos del objeto usando self:
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente


    # PRIMER MÉTODO: - retirar_dinero -
    def retirar_dinero(self, pCantidad):
        """
        Método para sustraer dinero del saldo, lanzando un error si no es posible.
        """

        # Validación - Control de flujo:
        if pCantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")

        elif pCantidad > self.saldo:
            raise ValueError("ERROR. No dispone de saldo suficiente en su cuenta corriente")

        else:
            self.saldo -= pCantidad  # self.saldo = self.saldo - pCantidad
            print(f"El usuario {self.nombre} retiró {pCantidad} con éxito. Saldo actual: {self.saldo}")


    # SEGUNDO MÉTODO: - transferir_dinero -
    def transferir_dinero(self, pUsuario, pCantidad):
        """
        Método para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
        """

        # Si el usuario no existe:
        if not pUsuario:
            raise ValueError("ERROR. El usuario no existe")

        else:
            # 1. Restar el saldo al emisor
            pUsuario.retirar_dinero(pCantidad)

            # 2. Sumar el saldo al receptor
            self.saldo += pCantidad  # self.saldo = self.saldo + pCantidad

            print("La transferencia fué realizada con éxito")


    # TERCERO MÉTODO: - agregar_dinero -
    def agregar_dinero(self, pCantidad):
        """
        Método para aumentar el saldo del usuario.
        """

        # Validación - Control de flujo:
        if pCantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que 0.")

        else:
            self.saldo += pCantidad
            print("La operación fué realizada con éxito")



# PRUEBAS - Caso de uso:


# a. Crear dos usuarios: "Alicia" con saldo inicial de 100
   # y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
usuario_Alicia = UsuarioBanco("Alicia", 100, True)
usuario_Bob = UsuarioBanco("Bob", 50, True)

print("--- Estado Inicial ---")
print("Alicia: \n"
      f"Nombre: {usuario_Alicia.nombre} \n"
      f"Saldo: {usuario_Alicia.saldo} \n"
      f"Cuenta Corriente: {usuario_Alicia.cuenta_corriente}")
print("Bob: \n" 
      f"Nombre: {usuario_Bob.nombre} \n"
      f"Saldo: {usuario_Bob.saldo} \n"
      f"Cuenta Corriente: {usuario_Bob.cuenta_corriente}")


# b. Agregar 20 unidades al saldo de Bob.

try: # try(teoría): encierra la operación propensa a fallos o código riesgoso
    usuario_Bob.agregar_dinero(20)

# MANEJO DE EXCEPCIONES:
# except(teoría): captura y maneja errores específicos, evitando la interrupción del programa.
except ValueError as error:
    print(f"Captura del error en agregación: {error}")


# c. Transferir 80 unidades de Bob a Alicia.

try:
    usuario_Alicia.transferir_dinero(usuario_Bob, 80)

# MANEJO DE EXCEPCIONES:
except ValueError as error:
    print(f"Captura del error en transferencia: {error}")


# d. Retirar 50 unidades del saldo de Alicia.

try:
    usuario_Alicia.retirar_dinero(50)

# MANEJO DE EXCEPCIONES:
except ValueError as error:
    print(f"Captura del error en retiro: {error}")


print("--- Estado Final de las Cuentas corrientes ---")
print(f"Saldo final de Alicia: {usuario_Alicia.saldo}")
print(f"Saldo final de Bob: {usuario_Bob.saldo}")
