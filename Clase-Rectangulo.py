class Rectangulo:
    def __init__(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self.__largo = largo
            self.__ancho = ancho
        else:
            raise ValueError("Las dimensiones iniciales deben ser mayores que cero.")

    # Método para cambiar dimensiones
    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("Error: El largo y el ancho deben ser mayores que cero.")

    # Método para consultar dimensiones actuales
    def consultar_dimensiones(self):
        return {"largo": self.__largo, "ancho": self.__ancho}

    # Método para calcular el área
    def calcular_area(self):
        return self.__largo * self.__ancho

    # Método para calcular el perímetro
    def calcular_perimetro(self):
        return 2 * (self.__largo + self.__ancho)

if __name__ == "__main__":
    r = Rectangulo(10, 5) 
    print(f"Área: {r.calcular_area()}")
    print(f"Perímetro: {r.calcular_perimetro()}")