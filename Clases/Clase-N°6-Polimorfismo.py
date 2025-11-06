import random
import time

class Vehiculos:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def moverse (self):
        f"El {self.nombre} se esta moviendo"

class Terrestre (Vehiculos):
    def __init__(self,nombre,rodar:str):
        super().__init__(Vehiculos)
        self.rodar = rodar

    def moverse(self):
        print(f"El coche {self.nombre} se esta moviendo")
        return self.rodar 

class Acuatico (Vehiculos):
    def __init__(self, nombre,navegar:str):
        super().__init__(Vehiculos)
        self.navegar = navegar

    def moverse(self):
        print(f"La lancha {self.nombre} esta navegando")
        return self.navegar

class Aereo (Vehiculos):
    def __init__(self, nombre, rodar:str, navegar:str):
        super().__init__(Vehiculos)
        self.rodar = rodar
        self.navegar = navegar

    def moverse(self):
        print(f"El avion {self.nombre} esta rodando y navegando")
        return self.rodar and self.navegar
        

class Hibrido (Vehiculos):
    def __init__(self, nombre, navegar:str, volar:str):
        super().__init__(Vehiculos)
        self.navegar = navegar
        self.volar = volar 

    def moverse(self):
        print (f"El hidroavion {self.nombre} esta navegando y volando")
        return self.navegar and self.volar
    

        



