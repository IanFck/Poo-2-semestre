class Coche:
    def __init__(self, marca: str, gasolina: float):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = 0

    def conducir(self, kilometros: float):
        litros_necesarios = kilometros / 10

        if self.gasolina >= litros_necesarios:
            self.kilometros_recorridos += kilometros
            self.gasolina -= litros_necesarios
            print(f"El coche {self.marca} recorrió {kilometros} km.")
        else:
            kilometros_posibles = self.gasolina * 10
            self.kilometros_recorridos += kilometros_posibles
            self.gasolina = 0
            print(f"El coche {self.marca} recorrió {kilometros_posibles} km y se quedó sin gasolina.")

    def cargar_gasolina(self, litros: float):
        self.gasolina += litros
        print(f"Se cargaron {litros} litros de gasolina. Total de gasolina: {self.gasolina} litros.")

mi_coche = Coche("Pagani", 10)
mi_coche.conducir(60)
mi_coche.cargar_gasolina(10)
mi_coche.conducir(120)

print(f"Kilometros totales: {mi_coche.kilometros_recorridos}")
print(f"Gasolina restante: {mi_coche.gasolina}")