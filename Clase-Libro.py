class Libro:
    def __init__(self, titulo, autor, total_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__total_paginas = total_paginas
        self.__pagina_actual = 1 # Empieza en la página 1

    def avanzar_paginas(self, paginas):
        if self.__pagina_actual + paginas <= self.__total_paginas:
            self.__pagina_actual += paginas
        else:
            raise ValueError("Error: No puedes avanzar más allá del total de páginas.")

    def retroceder_paginas(self, paginas):
        if self.__pagina_actual - paginas >= 1:
            self.__pagina_actual -= paginas
        else:
            raise ValueError("Error: No puedes retroceder antes de la página 1.")

    def consultar_pagina_actual(self):
        return self.__pagina_actual

    def obtener_informacion(self):
        return (f"Título: {self.__titulo}, Autor: {self.__autor}, "
                f"Total Páginas: {self.__total_paginas}, Página Actual: {self.__pagina_actual}")

# Prueba para la terminal
if __name__ == "__main__":
    mi_libro = Libro("El Principito", "García Márquez", 400)
    mi_libro.avanzar_paginas(50)
    print(mi_libro.obtener_informacion())
    mi_libro.retroceder_paginas(10)
    print(f"Página actual: {mi_libro.consultar_pagina_actual()}")