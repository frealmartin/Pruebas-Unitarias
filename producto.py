class Producto:
    # Constructor: se ejecuta al crear un nuevo producto
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.set_nombre(nombre)
        self.set_precio(precio)
        self.set_cantidad(cantidad)

    # Método para validar y asignar el nombre
    def set_nombre(self, nombre: str):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un texto no vacío.")
        self.nombre = nombre

    # Método para validar y asignar el precio
    def set_precio(self, precio: float):
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número mayor o igual a 0.")
        self.precio = float(precio)

    # Método para validar y asignar la cantidad en stock
    def set_cantidad(self, cantidad: int):
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero mayor o igual a 0.")
        self.cantidad = cantidad

    # Método para aumentar el stock disponible
    def agregar_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.cantidad += cantidad

    # Método para vender cierta cantidad de producto
    def vender(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser positiva.")
        if cantidad > self.cantidad:
            raise ValueError("No hay suficiente stock para realizar la venta.")
        self.cantidad -= cantidad

    # Representación del objeto como texto
    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio} - Stock: {self.cantidad}"
