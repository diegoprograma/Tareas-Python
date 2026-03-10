class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        """Inicializa los atributos del estudiante"""
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_estado(self):
        """Determina si el estudiante aprobó o reprobó (mínimo 3.5)"""
        if self.calificacion >= 3.5:
            return "Aprobado "
        else:
            return "Reprobado "

    def mostrar_datos(self):
        """Muestra la información completa del estudiante"""
        estado = self.verificar_estado()
        print(f"Estudiante: {self.nombre:<15}  Edad: {self.edad}  Nota: {self.calificacion} Estado: {estado}")


aula = [
    Estudiante("Ana García", 20, 2.0),
    Estudiante("Luis Pérez", 22, 3.5),
    Estudiante("María José", 19, 4.0),
    Estudiante("Carlos Ruiz", 21, 4.5),
    Estudiante("Elena Sanz", 20, 5.0)
]

print("--- REGISTRO ACADÉMICO DEL AULA ---")
for estudiante in aula:
    estudiante.mostrar_datos()