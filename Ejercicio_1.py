# PROGRAMACION ORIENTADA A OBJETOS
class CuentaBancaria:
    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance

    def generar_balance(self):
        print(self.balance)

    def depositar(self, deposito):
        if deposito>0:
            self.balance += deposito

mi_cuenta = CuentaBancaria("00980901234", "Ricardo Moreno", 50000)
#print (mi_cuenta.balance)


mi_cuenta.depositar(25000)
mi_cuenta.depositar(25000)
mi_cuenta.depositar(25000)

mi_cuenta.generar_balance()

