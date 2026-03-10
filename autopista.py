class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
        else:
            self.velocidad_actual = self.velocidad_maxima
        print(f"Acelerando... Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self, decremento):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            self.velocidad_actual = 0
        print(f"Frenando... Velocidad actual: {self.velocidad_actual} km/h")

    def verificar_limite(self, velocidad_limite):
        if self.velocidad_actual > velocidad_limite:
            print(f"⚠️ ¡ALERTA! Superas el límite de {velocidad_limite} km/h.")
        else:
            print(f"Vas a una velocidad segura (límite: {velocidad_limite} km/h).")

# --- Programa Principal con Menú ---

# Creamos el objeto inicial
mi_auto = Vehiculo("Toyota", "Corolla", 200)

while True:
    print(f"\n--- MONITOR DE: {mi_auto.marca} {mi_auto.modelo} ---")
    print(f"Velocidad actual: {mi_auto.velocidad_actual} km/h")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar límite de velocidad")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        inc = int(input("¿Cuánto quieres acelerar? (km/h): "))
        mi_auto.acelerar(inc)
    
    elif opcion == "2":
        dec = int(input("¿Cuánto quieres frenar? (km/h): "))
        mi_auto.frenar(dec)
    
    elif opcion == "3":
        lim = int(input("Ingresa el límite de la vía: "))
        mi_auto.verificar_limite(lim)
    
    elif opcion == "4":
        print("Saliendo del sistema de monitoreo... ¡Buen viaje!")
        break
    
    else:
        print("Opción no válida, intenta de nuevo.")