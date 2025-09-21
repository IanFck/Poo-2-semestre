#Tarea N°1/Lab1 - POO
#Ian Fack

#Aqui como dato dejaremos salud, vacunaciones y historial medico como datos privados, por ser datos sensibles
class Gato:
    def __init__(self, nombre, energia: int, edad: int, hambre: int):
        self.nombre = nombre
        self.energia = energia
        self.edad = edad
        self.hambre = hambre
        self.__salud = "Saludable" #Aqui definiremos la salud inicial en saludable
        self.__vacunaciones = []
        self.__historial_medico = []

    #Método: el gato juega baja su energia y sube hambre
    def jugar(self, gasto_energia: int, aumento_hambre: int):
        self.energia -= gasto_energia
        self.hambre += aumento_hambre
        self.__estado_de_salud()
        return f"El gato {self.nombre} está jugando. Energía: {self.energia}, Hambre: {self.hambre}"

    #Método: el gato come baja hambre y recupera energía
    def alimentar(self, comida: int, energia_recuperada: int):
        self.hambre = max(0, self.hambre - comida)  # hambre no puede ser negativa
        self.energia += energia_recuperada
        self.__estado_de_salud() 
        return f"El gato {self.nombre} se alimentó. Energía: {self.energia}, Hambre: {self.hambre}"

    #Método estado de salud (Privado)
    #Para este metodo, pensaremos un poco como notamos a los gatos cuando estan mal, y segun los atributos
    #que tenemos, podriamos definirlos cuando este nbajos de hambre y de energia
    def __estado_de_salud(self):
        if self.hambre >= 80 or self.energia < 20:
            self.__salud = "Gatito Enfermo"
        elif 50 <= self.hambre < 80:
            self.__salud = "Gatito en observación"
        else:
            self.__salud = "Gatito saludable"
            self.__historial_medico.append(f"Actualizacion de historial! :{self.__salud}")
        
    #Método para poder ver el historial del gato   
    def mostrar_historial(self):
        return f"Historial medico del gatito:{self.__historial_medico}"

    #Método para ver la salud del gatito  
    def salud_de_gato(self):
        return self.__salud
    
    #Métodos para las vacunas
    #Método para agregar una vacunacion a un gatito
    def agregar_vacunas (self, vacuna:str):
        self.__vacunaciones.append(vacuna)
        self.__historial_medico.append(f"El gatito:{self.nombre} recibio la vacuna: {vacuna}")

    #Método para ver las vacunas que tiene el gatito
    def mostrar_vacunaciones (self):
        if not self.__vacunaciones:
            return f"El gatito {self.nombre} no tiene una vacuna registrada"
        return f"Las vacunas del gatito {self.nombre}:{', '.join(self.__vacunaciones)}"

    #Método: imprimir información del gatito
    def __str__(self):
        return f"Gatito: {self.nombre}, Edad: {self.edad}, Energía: {self.energia}, Hambre: {self.hambre}, Salud: {self.__salud}"

    #Método: finalizador
    def __del__(self):
        print(f"El gatito {self.nombre} ha salido del café.")

class Espacio:
    def __init__(self, nombre_del_lugar: str, capacidad_maxima: int):
        self.nombre_del_lugar = nombre_del_lugar
        self.capacidad_maxima = capacidad_maxima
        self.gatos_en_lugar = []

    #Agregar gato al espacio, si hay capacidad disponible
    def agregar_gato(self, gato: Gato):
        if len(self.gatos_en_lugar) < self.capacidad_maxima:
            if gato not in self.gatos_en_lugar:
                self.gatos_en_lugar.append(gato)
                return f"Se agregó el gato {gato.nombre} al {self.nombre_del_lugar}."
            else:
                return f"El gato {gato.nombre} ya está en el {self.nombre_del_lugar}."
        else:
            return f"No se puede agregar más gatos, capacidad máxima alcanzada en {self.nombre_del_lugar}."

    #Mostrar información de los gatos presentes en el espacio
    def mostrar_gatos(self):
        if not self.gatos_en_lugar:
            return f"No hay gatos en {self.nombre_del_lugar}."
        info = f"Gatos en {self.nombre_del_lugar}:\n"
        for g in self.gatos_en_lugar:
            info += f"- {g.nombre}, Edad: {g.edad}\n"
        return info

    def __str__(self):
        return f"Espacio: {self.nombre_del_lugar}, Capacidad: {self.capacidad_maxima}, Gatos presentes: {len(self.gatos_en_lugar)}"


#Crear gatos
Gatito1 = Gato("Michi", 100, 3, 20)
Gatito2 = Gato("Pepito", 80, 2, 40)
Gatito3 = Gato("Chocokat", 60, 5,30)

#Crear espacios
terraza = Espacio("Terraza", 2)
entrada = Espacio("Entrada", 1)

#Mostrar información inicial
print(Gatito1)
print(Gatito2)
print(Gatito3)

#Acciones de gatos
print(Gatito1.jugar(20, 10))
print(Gatito2.alimentar(15, 20))

#Historial Medico de los gatos
print("Historial médico de Michi:")
print(Gatito1.mostrar_historial())
print("--------------------")
print("Historial médico de Pepito:")
print(Gatito2.mostrar_historial())
print("--------------------")
print("Historial médico de Chocokat:")
print(Gatito3.mostrar_historial())

#Agregar las vacunas a nuestros gatitos
print(Gatito1.agregar_vacunas("Antirrábica"))
print(Gatito2.agregar_vacunas("Triple Felina"))
print(Gatito3.agregar_vacunas("Rinotraqueítis"))

#Visualizar las vacunacioens que agregamos
print(Gatito1.mostrar_vacunaciones())
print(Gatito2.mostrar_vacunaciones())
print(Gatito3.mostrar_vacunaciones())


#Probar espacios
print(terraza.agregar_gato(Gatito1))
print(terraza.agregar_gato(Gatito2))
print(terraza.agregar_gato(Gatito3)) 

print(terraza.mostrar_gatos())
print(entrada.mostrar_gatos())