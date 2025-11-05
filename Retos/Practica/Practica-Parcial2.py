# Practica Parcial
# Ejercicio: Clase CuentaBancaria

class CuentaBancaria:

    def __init__(self, titular: str, saldo: int):
        self.__titular = titular
        self.__saldo = saldo

    # Getter
    @property
    def saldo(self):
        return self.__saldo

    # Setter
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print("El saldo no puede ser negativo.")
        else:
            self.__saldo = nuevo_saldo
            print(f"Saldo actualizado: ${self.__saldo}")

    # Método depositar
    def depositar(self, dinero):
        if dinero > 0:
            self.__saldo += dinero
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("Error: el monto debe ser positivo.")

cuenta1 = CuentaBancaria("Ian", 1000)
cuenta1.depositar(500)
cuenta1.depositar(-50)
cuenta1.saldo = 2000
cuenta1.saldo = -100
print(cuenta1.saldo)
