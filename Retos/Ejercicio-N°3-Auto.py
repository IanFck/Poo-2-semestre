class Vehiculo:
    def __init__(self, marca, modelo, año: int):
        self.__marca = marca 
        self.__modelo = modelo
        self.__año = año 
        self.__disponible = True

    def marcar_vendido(self):
        if self.__disponible:
            self.__disponible = False
            return f"El vehiculo: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año} se a vendido, No esta disponible"
        
    def __str__(self):
        return f"Vehiculo: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año} Estado: {self.__disponible} (True=Disponible)"

class Concesionario:
    def __init__(self):
        self.vehiculos = []  

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)
        return f"Vehículo agregado: {vehiculo}"

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            return "No se encuentran vehículos en la concesionaria."
        lista = "\n".join([f"{i+1}. {v}" for i, v in enumerate(self.vehiculos)])
        return f"Vehículos en la concesionaria:{lista}"

    def vender_vehiculo(self, indice: int):
        if 1 <= indice <= len(self.vehiculos):
            vehiculo = self.vehiculos[indice - 1]
            return vehiculo.marcar_vendido()
        else:
            return "Número de vehículo inválido."


vehiculo1 = Vehiculo("Mclaren", "MP4-17", 2002)
vehiculo2 = Vehiculo("Chevrolet", "Camaro", 2003)

concesionario = Concesionario()
print(concesionario.agregar_vehiculo(vehiculo1))
print(concesionario.agregar_vehiculo(vehiculo2))

print(concesionario.mostrar_vehiculos())