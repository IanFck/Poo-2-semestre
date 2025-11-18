# Clase Metodo de pago
class MetodoDePago:
    def procesar_pago (self, monto):
        raise NotImplementedError("Las subclases deben implementar procesar_pago(monto)")
    
# Clase para la validacion
class RequiereValidacion:
    def validar(self):
        raise NotImplementedError("Subclase debe implementar validar()")

# Clase para la confirmacion
class RequiereConfirmacion:
    def confirmar(self, codigo):
        raise NotImplementedError("Subclase debe implementar confirmar(codigo)")
    
# Clase para la tarjeta de credito
class TarjetaCredito(MetodoDePago, RequiereValidacion):
    def __init__(self, numero):
        self.numero = numero

# Simulacion de la validacion con el numero de la tarjeta
def validar(self):
        print(f"[TarjetaCredito] Validando tarjeta {self.numero}...")
        return True

# Def de procesar pago, si no se pude validar, la tarjeta queda fallida y si pasa, pasara a procesar el pago 
def procesar_pago(self, monto):
        if not self.validar():
            raise Exception("Validación de tarjeta fallida")
        print(f"[TarjetaCredito] Procesando pago con tarjeta por ${monto}")

class TarjetaDebito(MetodoDePago, RequiereValidacion):
    def __init__(self, cuenta):
        self.cuenta = cuenta
        self.confirmado = False

# Def para confirmar la tarjeta de debito
    def confirmar(self, cvv):
        print(f"[TarjetaDebito] Confirmando transferencia con Cvv: {cvv}")
        # El cvv siempre sera correcto
        self.confirmado = True
        return True
    
# Def para procesar el pago
    def procesar_pago(self, monto):
        # la clase asume que se ha confirmado previamente; si no, puede lanzar.
        if not getattr(self, "confirmado", False):
            raise Exception("Transferencia no confirmada")
        print(f"[TarjetaDebito] Procesando transferencia por ${monto}")

class PagoEfectivo(MetodoDePago):
    def procesar_pago(self, monto):
        # no necesita validación ni confirmación, solo registra el monto
        print(f"[PagoEfectivo] Registrando pago en efectivo por ${monto}")
    
def ejecutar_pago(metodo: MetodoDePago, monto, *, codigo_confirmacion=None):

    if hasattr(metodo, "validar"):
        resultado = metodo.validar()
        if resultado is False:
            raise Exception("Validación fallida - no se procesará el pago")
        
    if hasattr(metodo, "confirmar"):
        if codigo_confirmacion is not None:
            metodo.confirmar(codigo_confirmacion)
        else:
            # si la implementación de procesar_pago espera confirmación previa,
            # dejar que ella maneje la excepción o avisar:
            print("[ejecutar_pago] Atención: el método soporta confirmación y no se proporcionó código.")
        

    metodo.procesar_pago(monto)

if __name__ == "__main__":
    efectivo = PagoEfectivo()
    tarjeta = TarjetaCredito(numero="1234-5678-9012-3456")
    Debito = TarjetaDebito(cuenta="CL-12345678")

    print("--- Pago en efectivo ---")
    ejecutar_pago(efectivo, 1000)

    print("\n--- Pago con tarjeta ---")
    ejecutar_pago(tarjeta, 15000)

    print("\n--- Transferencia sin código (advertencia) ---")
    try:
        ejecutar_pago(Debito, 8000)  # advertencia: no mandamos código
    except Exception as e:
        print("Error:", e)

    print("\n--- Transferencia con confirmación ---")
    ejecutar_pago(Debito, 8000, codigo_confirmacion="ABC-123")

