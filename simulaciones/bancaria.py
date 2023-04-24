class CuentaBanco():
    def __init__(self,saldo_inicial=0):
        self.saldo=saldo_inicial
    def ingresar(self,cantidad):
        self.saldo += cantidad
    def retirar(self,cantidad):
        if self.saldo < cantidad:
         raise ValueError("No hay suficiente saldo")
        self.saldo -= cantidad
    def consultar(self):
        return self.saldo
    
import unittest

class TestCuentaBanco(unittest.TestCase):
    def test_ingresar(self):
        cuenta=CuentaBanco(saldo_inicial=0)
        cuenta.ingresar(100)
        self.assertEqual(cuenta.obtener_saldo(),100)

    def test_retirar(self):
        cuenta=CuentaBanco(saldo_inicial=100)
        cuenta.retirar(50)
        self.assertEqual(cuenta.obtener_saldo(),50)
    
    def test_retirar_insuficiente(self):
        cuenta = CuentaBanco(saldo_inicial=100)
        with self.assertRaises(ValueError):
            cuenta.retirar(200)
    
    
    def test_obtener_saldo(self):
        cuenta=CuentaBanco(saldo_inicial=100)
        self.assertEqual(cuenta.obtener_saldo(),100)



class TestCuentaBancoIntegracion(unittest.TestCase):
    def test_procesos_ingreso_retiro(self):
        cuenta=CuentaBanco(saldo_inicial=100)
        procesosIngreso= [100]*40 + [50]*20 + [20]*60
        procesosRetiro= [100]*40 + [50]*20 + [20]*60

        def proceso_ingreso(cantidad):
            cuenta.ingresar(cantidad)

        def proceso_retiro(cantidad):
            cuenta.retirar(cantidad)


        import multiprocessing
        pool = multiprocessing.Pool()
        pool.map(proceso_ingreso, procesosIngreso)
        pool.map(proceso_retiro, procesosRetiro)
        pool.close()
        pool.join()
        self.assertEqual(cuenta.obtener_saldo(), 100)
        
        print("El saldo final es: " + str(cuenta.obtener_saldo()))

if __name__ == '__main__':
    unittest.main()






