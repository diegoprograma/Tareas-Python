class TarjetaCredito:
    def __init__(self, numero):
        self.__numero = str(numero)

    @staticmethod
    def validar_tarjeta(numero):
        n_tarjeta = str(numero).replace(" ", "")
        suma = 0
        reverso = n_tarjeta[::-1] 
        
        for i, digito in enumerate(reverso):
            n = int(digito)
            if i % 2 == 1: 
                n *= 2
                if n > 9:
                    n -= 9
            suma += n
            
        return suma % 10 == 0

# Prueba en terminal
if __name__ == "__main__":
    num_test = "79927398713" 
    es_valida = TarjetaCredito.validar_tarjeta(num_test)
    
    print(f"¿La tarjeta {num_test} es válida?: {es_valida}")