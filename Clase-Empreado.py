class Empleado:
    total_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.total_empleados += 1

    @classmethod
    def cantidad_empleados(cls):
        return f"Total de empleados registrados: {cls.total_empleados}"


if __name__ == "__main__":
    e1 = Empleado("Ana", 2500)
    e2 = Empleado("Luis", 3000)
    e3 = Empleado("Marta", 2800)
    e4 = Empleado("Carlos", 3200)
    e5 = Empleado("Sofia", 2700)
    print(Empleado.cantidad_empleados()) 