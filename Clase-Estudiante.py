class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = [] # Lista privada de notas

    def agregar_nota(self, nota):
        if 0 <= nota <= 5.0:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 5.0.")

    def calcular_promedio(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

# Prueba para la terminal
if __name__ == "__main__":
    est = Estudiante("Diego", 20)
    est.agregar_nota(3.0)
    est.agregar_nota(5.0)
    print(f"Estudiante: {est.obtener_nombre()}")
    print(f"Promedio: {est.calcular_promedio()}")