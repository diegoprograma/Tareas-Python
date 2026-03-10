class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        """Devuelve True si hay suficiente stock, False si no."""
        if self.stock >= cantidad:
            print(f"Hay disponibilidad para {cantidad} unidades de {self.nombre}.")
            return True
        else:
            print(f"No hay suficiente stock. Solo quedan {self.stock} unidades.")
            return False

    def vender(self, cantidad):
        """Reduce el stock si es posible."""
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f" Venta realizada: {cantidad} unidades. Nuevo stock: {self.stock}")
        else:
            print(f"Venta cancelada por falta de existencias.")

    def reabastecer(self, cantidad):
        """Aumenta el stock del producto."""
        self.stock += cantidad
        print(f"Reabastecimiento: Se han añadido {cantidad} unidades. Stock total: {self.stock}")

# --- Ejecución de las operaciones solicitadas ---

# 1. Crear el objeto inicial
mi_laptop = Producto("Laptop", 1200, 10)

print(f"--- Iniciando gestión de {mi_laptop.nombre} ---")

# 2. Verificar si hay 5 unidades disponibles
mi_laptop.verificar_disponibilidad(5)

# 3. Vender 3 unidades
mi_laptop.vender(3)

# 4. Verificar si hay 8 unidades disponibles
mi_laptop.verificar_disponibilidad(8)

# 5. Intentar vender 8 unidades (debe fallar)
mi_laptop.vender(8)

# 6. Reabastecer con 10 unidades adicionales
mi_laptop.reabastecer(10)

# 7. Verificar nuevamente si hay 8 unidades y venderlas
if mi_laptop.verificar_disponibilidad(8):
    mi_laptop.vender(8)