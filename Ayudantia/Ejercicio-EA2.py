# 1. Clase base Trabajador - Debe tener un atributo nombre. 
class Trabajador ():
    def __init__(self, nombre):
        self.nombre = nombre 

    # Debe implementar un método tarea() que retorne un mensaje genérico indicando que realiza tareas generales.
    def tarea (self):
        return f"{self.nombre} esta haciendo una tarea en general"
    
# 2. Clase Chef que hereda de Trabajador, debe agregar el atributo especialidad.Debe sobrescribir tarea() indicando qué prepara el chef.
class Chef (Trabajador):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad

    def tarea(self):
        return f"{self.nombre} esta cocinando un plato de la especialidad {self.especialidad}"

# 3. Clase Mesero que hereda de Trabajador - Debe agregar el atributo seccion. - Debe sobrescribir tarea() indicando qué sección atiende.
class Mesero (Trabajador):
    def __init__(self, nombre, seccion):
        super().__init__(nombre)
        self.seccion = seccion

    def tarea(self):
        return f"{self.nombre} esta en la {self.seccion} atendiendo"  

# 4. Clase AyudanteChefMesero (Herencia múltiple) - Debe heredar de Chef y Mesero. Constructor recibe: nombre, especialidad, seccion. - Debe sobrescribir tarea() combinando ambas funciones.
class AyudanteChefMesero (Chef,Mesero):
    def __init__(self, nombre, seccion, especialidad):
            Chef.__init__(nombre, especialidad)
            Mesero.__init__(seccion)
            self.especialidad = especialidad

    def tarea(self):
        return f"El {self.nombre} esta cocinando en la seccion {self.seccion} y tiene la especialidad de {self.especialidad}"
    

Primer_Trabajador = Trabajador("Luis")
print(Primer_Trabajador.tarea())

Primer_Chef = Chef("Claudio", "Carne a la Plancha")
print(Primer_Chef.tarea())

Primer_mesero = Mesero("Sofia", "Atención al cliente")
print(Primer_mesero.tarea())

Primer_ayudante = AyudanteChefMesero("Ian", "Platos especiales", "Maestro de Chef")
print(Primer_Trabajador.tarea())



