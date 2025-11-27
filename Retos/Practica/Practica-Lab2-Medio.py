# Nivel medio/ crear clase Empleado
class Empleado():
    def __init__(self, nombre):
        self.nombre = nombre

class Programador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def codificar(self):
        return f"El {self.nombre} esta codificando"
    
class Diseñador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def diseñar(self):
        return f"El {self.nombre} esta diseñando"
    
class DesarrolladorFullStack (Diseñador,Programador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar (self):
        return f"{self.codificar()} y {self.diseñar()}"
    
Empleado1 = DesarrolladorFullStack("Ian")
print(Empleado1.trabajar())