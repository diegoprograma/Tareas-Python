class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_informacion(self):
        print(f"Información del Libro")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.paginas}")
        print("-" * 30)

    def actualizar_paginas(self, nuevas_paginas):
        if nuevas_paginas > 0:
            self.paginas = nuevas_paginas
            print(f"El número de páginas de '{self.titulo}' ha sido actualizado a {nuevas_paginas}.")
        else:
            print("Error: El número de páginas debe ser mayor a 0.")

# Ejemplo de uso

#Creamos un objeto de la clase Libro
mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez", 500)
#Mostramos la información inicial
mi_libro.mostrar_informacion()
#Actualizamos el número de páginas
mi_libro.actualizar_paginas(2)
#Mostramos la información actualizada
mi_libro.mostrar_informacion()

mi_libro = Libro("El principito", "Luis Marquez", 500)
mi_libro.mostrar_informacion()
mi_libro.actualizar_paginas(3)
mi_libro.mostrar_informacion()

mi_libro = Libro("El principito", "Luis Marquez", 500)
mi_libro.mostrar_informacion()
mi_libro.actualizar_paginas(3)
mi_libro.mostrar_informacion()

mi_libro = Libro("El principito", "Luis Marquez", 500)
mi_libro.mostrar_informacion()
mi_libro.actualizar_paginas(3)
mi_libro.mostrar_informacion()