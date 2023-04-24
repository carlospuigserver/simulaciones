class CuentaBanco():
    def __init__(self,saldoI=0):
        self.saldo=saldoI
    def ingresar(self,cantidad):
        self.saldo += cantidad
    def retirar(self,cantidad):
        self.saldo -= cantidad
    def consultar(self):
        return self.saldo
    
import unittest

class TestCuentaBanco(unittest.TestCase):
    def test_ingresaar(self):
        cuenta=CuentaBanco(saldo_inicial=0)
        cuenta.ingresar(100)
        self.assertEqual(cuenta.obtener_saldo(),100)

    def test_retirar(self):
        cuenta=CuentaBanco(saldo_inicial=100)
        cuenta.retirar(50)
        self.assertEqual(cuenta.obtener_saldo(),50)
    def test_obtener_saldo(self):
        cuenta=CuentaBanco(saldo_inicial=100)
        self.assertEqual(cuenta.obtener_saldo(),100)