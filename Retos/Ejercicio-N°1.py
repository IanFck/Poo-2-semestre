
nota1 = input(float("Ingresa tu primera nota"))
nota2 = input(float("Ingresa tu segunda nota"))
nota3 = input(float("Ingresa tu tercera nota"))

class Persona():

    def __init__(self, nombre, apellido, edad, altura, peso): # self es una palabra NO reservada siendo una referencia a si mismo. este método se ejecuta automáticamente al crear un nuevo objeto
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.altura = float (altura)
        self.peso = float (peso)

    def calcular_imc (self):
        imc = self.peso/self.altura^2
        print(f"{self.nombre} es su imc")

    #if calcular_imc     

    def promedio_asignatura (self):
        print(f"{self.nombre} es su promedio de la asignatura")


Humano1 = Persona("Ian", "Fack", "22", "1.73", "60.4")
Humano2 = Persona("Luis", "Muñoz", "18", "1.78", "80.3")
Humano3 = Persona("Dayana", "Levicoy", "19", "1.58", "64.9")

print (f"El nombre del Humano es: {Humano1.nombre}, tiene el apellido: {Humano1.apellido}, su edad es: {Humano1.edad}, la altura es: {Humano1.altura} y su peso es: {Humano1.peso}")
print (f"El nombre del Humano es: {Humano2.nombre}, tiene el apellido: {Humano2.apellido}, su edad es: {Humano2.edad}, la altura es: {Humano2.altura} y su peso es: {Humano2.peso}")
print (f"El nombre del Humano es: {Humano3.nombre}, tiene el apellido: {Humano3.apellido}, su edad es: {Humano3.edad}, la altura es: {Humano3.altura} y su peso es: {Humano3.peso}")
