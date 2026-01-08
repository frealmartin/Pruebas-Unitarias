import unittest
from producto import Producto

class TestProducto(unittest.TestCase):

    def setUp(self):
        print("\n--- Configurando producto de prueba ---")
        self.producto = Producto("Teclado", 25.5, 10)
        print(f"Producto creado: {self.producto}")

    def test_nombre_valido(self):
        print("✅ Probando que el nombre se asigna correctamente")
        self.assertEqual(self.producto.nombre, "Teclado")

    def test_precio_valido(self):
        print("✅ Probando que el precio se asigna correctamente")
        self.assertEqual(self.producto.precio, 25.5)

    def test_cantidad_valida(self):
        print("✅ Probando que la cantidad se asigna correctamente")
        self.assertEqual(self.producto.cantidad, 10)

    def test_nombre_invalido(self):
        print("❌ Probando que no se acepta un nombre vacío")
        with self.assertRaises(ValueError):
            Producto("", 10.0, 5)

    def test_precio_negativo(self):
        print("❌ Probando que no se acepta un precio negativo")
        with self.assertRaises(ValueError):
            Producto("Monitor", -50, 5)

    def test_cantidad_negativa(self):
        print("❌ Probando que no se acepta una cantidad negativa")
        with self.assertRaises(ValueError):
            Producto("Ratón", 15.0, -2)

    def test_agregar_stock(self):
        print("🔄 Probando que se puede aumentar el stock")
        self.producto.agregar_stock(5)
        self.assertEqual(self.producto.cantidad, 15)

    def test_agregar_stock_invalido(self):
        print("❌ Probando que no se puede agregar stock con cantidad 0")
        with self.assertRaises(ValueError):
            self.producto.agregar_stock(0)

    def test_vender_producto(self):
        print("🔄 Probando que se puede vender parte del stock")
        self.producto.vender(3)
        self.assertEqual(self.producto.cantidad, 7)

    def test_vender_mas_de_lo_que_hay(self):
        print("❌ Probando que no se puede vender más stock del disponible")
        with self.assertRaises(ValueError):
            self.producto.vender(25)

    def test_vender_cantidad_invalida(self):
        print("❌ Probando que no se puede vender cantidad 0")
        with self.assertRaises(ValueError):
            self.producto.vender(0)

if __name__ == '__main__':
    unittest.main()
