class Vehiculo:
    def __init__(self, marca, modelo, año: int):
        self.__marca = marca 
        self.__modelo = modelo
        self.__año = año 
        self.__disponible = True

    def marcar_vendido(self):
        return f"El vehiculo: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año} se a vendido, No esta disponible"
        self.__disponible = False
    
    def __str__(self):
        return f"Vehiculo: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año} Estado: {self.__disponible} (True=Disponible)"

class Concesionario ():
    def __init__(self):
        self.Vehiculos = []

    def agregar_vehiculos(self, Vehiculos: Vehiculo):
        return f"Agregando vehiculos al concesionario"
        self.Vehiculos.append(Vehiculos)

    def mostrar_vehiculos(self):
        if not self.Vehiculos:
            return f"No se encuentran vehiculos en {self.Vehiculos}"
        


Vehiculo1 = Vehiculo("Mclaren", "MP4-17", 2002)
Vehiculo2 = Vehiculo("Chevloret", "Camaro", 2003)
print(Vehiculo1.marcar_vendido())
print(Vehiculo2)


        