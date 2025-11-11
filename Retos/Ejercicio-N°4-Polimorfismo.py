class Animal:
    def __init__(self, nombre, edad, peso, genero):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.genero = genero

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")
    def mostrar_ficha(self):
        print(f"{self.nombre}, tiene {self.edad} años, pesa {self.peso} kg, y es {self.genero}")

class Perro(Animal):
    def __init__(self, nombre, edad, raza, peso, genero):
        super().__init__(nombre, edad, peso, genero)
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando")


class Gato(Animal):
    def __init__(self, nombre, edad, color_pelaje, peso, genero):
        super().__init__(nombre, edad, peso, genero)
        self.color_pelaje = color_pelaje

    def maullar(self):
        print(f"{self.nombre} está maullando")

class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, genero, color_plumaje):
        super().__init__(nombre, edad, peso, genero)
        self.genero = genero
        self.color_plumaje = color_plumaje
    def volar(self):
        return f"{self.nombre} está volando alto"
    
    def mostrar_ficha(self):
        super().mostrar_ficha() 
        print(f"Color de plumaje: {self.color_plumaje}")
    
Animal1 = Animal("Pepito",2,10,"Hembra")
Perro1 = Perro("Salchicha",3,"Salchicha",5,"Macho")
Gato1= Gato("Michi",3,"Blanco",6,"Macho")
Pajaro1 = Pajaro("Lorito",2,2,"Macho","Amarillo")

#COMER
Animal1.comer()
Perro1.comer()
Gato1.comer()
Pajaro1.comer()

#DORMIR
Animal1.dormir()
Perro1.dormir()
Gato1.dormir()
Pajaro1.dormir()

#MOSTRAR FICHA
Animal1.mostrar_ficha()

#LADRAR    
Perro1.ladrar()

#MAULLAR
Gato1.maullar()

#VOLAR
Pajaro1.volar()

#MOSTRAR FICHA PAJARA
Pajaro1.mostrar_ficha()