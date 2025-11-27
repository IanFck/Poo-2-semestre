# Crear clase Dispositivo
class Dispositivo:
    def __init__(self, marca: str):
        self.marca = marca

class Celular(Dispositivo):
    def __init__(self, marca):
        super().__init__(marca)

    def llamar(self):
        return f"Llamando"

class Camara(Dispositivo):
    def __init__(self, marca):
        super().__init__(marca)

    def sacar_foto(self):
        return f"Sacando foto"

class SmartPhone(Celular, Camara):
    def __init__(self, marca):
        super().__init__(marca)  # Gracias al MRO, solo se llama una vez

    def usar(self):
        return f"{self.llamar()} y {self.sacar_foto()}"

Telefono = SmartPhone("Samsung")
print(Telefono.usar())




