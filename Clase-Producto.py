class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        # Validamos el precio inicial también
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio inicial debe ser mayor que cero.")

    # Método para consultar el nombre
    def obtener_nombre(self):
        return self.__nombre

    # Método para consultar el precio actual
    def consultar_precio(self):
        return self.__precio

    # Método para cambiar el precio con validación
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("Error: El nuevo precio debe ser mayor que cero.")

    # Método para aplicar un descuento (0 a 100)
    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            descuento = self.__precio * (porcentaje / 100)
            self.__precio -= descuento
        else:
            raise ValueError("Error: El porcentaje debe estar entre 0 y 100.")

# Ejemplo de uso:
p = Producto(" Computadora ", 1000)
p.aplicar_descuento(10)
print(p.consultar_precio()) # 900.0