class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self._saldo = saldo_inicial  

    def consultar_saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
        else:
            print("Monto inválido")

# --- Clase CuentaAhorro que extiende a CuentaBancaria ---
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, interes_anual):
        # Llamamos al constructor de la clase padre
        super().__init__(titular, saldo_inicial)
        self.__interes_anual = interes_anual # Atributo privado nuevo

    def aplicar_interes(self):
        # El interés se calcula sobre el saldo actual
        interes = self._saldo * (self.__interes_anual / 100)
        self._saldo += interes
        print(f"Interés aplicado: +{interes}")

    def consultar_interes(self):
        return self.__interes_anual

# --- Ejemplo de uso ---
if __name__ == "__main__":
    mi_cuenta = CuentaAhorro("Diego", 1000, 5) 
    print(f"Saldo inicial: {mi_cuenta.consultar_saldo()}")
    
    mi_cuenta.aplicar_interes()
    print(f"Saldo tras interés: {mi_cuenta.consultar_saldo()}")
    print(f"Porcentaje de interés: {mi_cuenta.consultar_interes()}%")