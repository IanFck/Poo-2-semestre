# Nivel Difícil (4 ejercicios) — combinan MRO, super y atributos
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def estudiar(self):
        return f"La persona {self.nombre} con edad: {self.edad} esta estudiando"
    
class Trabajador(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def trabajar(self):
        return f"La persona {self.nombre} con edad: {self.edad} esta trabajando"
    
class EstudianteTrabajador (Estudiante,Trabajador):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def funciones(self):
        return f"{self.estudiar()} y {self.trabajar()}"
    
P1 = EstudianteTrabajador("Luis", 22)
print(P1.funciones())