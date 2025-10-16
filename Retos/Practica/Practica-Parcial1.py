# Ejercicio 1:
# Crear una clase Persona que encapsule los atributos privados __nombre y __edad.
class Persona:
    def __init__(self, nombre:str, edad:int):
        self.__nombre = nombre

        assert edad>= 0, "La edad no puede ser negativa"
        self.__edad = edad

    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            print("Error: la edad no puede ser negativa")
        else:
            self.__edad = nueva_edad

    # Método para mostrar datos
    def mostrar(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

# Prueba
p = Persona("Ian", 21)
p.mostrar()
p.set_edad(-5)  # Mensaje de error
p.set_nombre("Andres")
p.mostrar()