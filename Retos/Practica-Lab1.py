class Estudiante():
    def __init__(self, nombre, apellido, notas:float):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def mostrar_info(self):
        promedio = self.calcular_promedio()
        return f"El nombre del alumno es: {self.nombre}, su apellido es: {self.apellido} y su promedio es {promedio:.2f}"
    
A1 = Estudiante("Ian", "Fack", [5.4, 6.0, 5.8])
A2 = Estudiante("Alejandro", "Bustos", [3.2, 4.0, 4.5])

print (A1.mostrar_info())
print (A2.mostrar_info())


