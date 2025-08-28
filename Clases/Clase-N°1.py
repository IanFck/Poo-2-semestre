#Lo primero crear una clase con el comando class y poniendo el nombre de la clase, la primer letra con mayuscula
class Persona():
    
    # Constructor de Clase
    #Se crea con un def, siendo una funcion especial para crear objetos, por el momento usar la palabra self
    #Aributos de la clase
    def __init__(self, nombre, apellido, edad): # self es una palabra NO reservada siendo una referencia a si mismo. este método se ejecuta automáticamente al crear un nuevo objeto
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad

    #Metodos (comportamientos)

    def correr (self): #self permite acceder al kas funciones
        print(f"{self.nombre} esta corriendo")

    def dormir (self):
        print(f"{self.nombre} esta durmiendo")

Humano1 = Persona("Ian", "Fack", "22")
Humano2 = Persona("Luis", "Muñoz", "18")
Humano3 = Persona("Dayana", "Levicoy", "19")

print (f"El nombre del Humano es: {Humano1.nombre}, tiene el apellido: {Humano1.apellido}, y su edad es: {Humano1.edad}")
print (f"El nombre del Humano es: {Humano2.nombre}, tiene el apellido: {Humano2.apellido}, y su edad es: {Humano2.edad}")
print (f"El nombre del Humano es: {Humano3.nombre}, tiene el apellido: {Humano3.apellido}, y su edad es: {Humano3.edad}")


# Llamana de los metodos 
Humano1.correr
Humano2.dormir