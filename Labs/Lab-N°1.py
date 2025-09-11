#Lab N°1 - POO
#Ian Fack

class Gato:
    def __init__(self, nombre, energia: int, edad: int, hambre: int):
        self.nombre = nombre
        self.energia = energia
        self.edad = edad
        self.hambre = hambre

    # Método: el gato juega → baja energia, sube hambre
    def jugar(self, gasto_energia: int, aumento_hambre: int):
        self.energia -= gasto_energia
        self.hambre += aumento_hambre
        return f"El gato {self.nombre} está jugando. Energía: {self.energia}, Hambre: {self.hambre}"

    # Método: el gato come → baja hambre y recupera energía
    def alimentar(self, comida: int, energia_recuperada: int):
        self.hambre = max(0, self.hambre - comida)  # hambre no puede ser negativa
        self.energia += energia_recuperada
        return f"El gato {self.nombre} se alimentó. Energía: {self.energia}, Hambre: {self.hambre}"

    # Método: imprimir información clara del gato
    def __str__(self):
        return f"Gato: {self.nombre}, Edad: {self.edad}, Energía: {self.energia}, Hambre: {self.hambre}"

    # Método: finalizador
    def __del__(self):
        print(f"El gato {self.nombre} ha salido del café.")

class Espacio:
    def __init__(self, nombre_del_lugar: str, capacidad_maxima: int):
        self.nombre_del_lugar = nombre_del_lugar
        self.capacidad_maxima = capacidad_maxima
        self.gatos_en_lugar = []

    # Agregar gato al espacio, si hay capacidad disponible
    def agregar_gato(self, gato: Gato):
        if len(self.gatos_en_lugar) < self.capacidad_maxima:
            if gato not in self.gatos_en_lugar:
                self.gatos_en_lugar.append(gato)
                return f"Se agregó el gato {gato.nombre} al {self.nombre_del_lugar}."
            else:
                return f"El gato {gato.nombre} ya está en el {self.nombre_del_lugar}."
        else:
            return f"No se puede agregar más gatos, capacidad máxima alcanzada en {self.nombre_del_lugar}."

    # Mostrar información de los gatos presentes en el espacio
    def mostrar_gatos(self):
        if not self.gatos_en_lugar:
            return f"No hay gatos en {self.nombre_del_lugar}."
        info = f"Gatos en {self.nombre_del_lugar}:\n"
        for g in self.gatos_en_lugar:
            info += f"- {g.nombre}, Edad: {g.edad}\n"
        return info

    def __str__(self):
        return f"Espacio: {self.nombre_del_lugar}, Capacidad: {self.capacidad_maxima}, Gatos presentes: {len(self.gatos_en_lugar)}"


# Crear gatos
g1 = Gato("Michi", 100, 3, 20)
g2 = Gato("Pepito", 80, 2, 40)
g3 = Gato("Chocokat", 60, 5, 30)

# Crear espacios
terraza = Espacio("Terraza", 2)
entrada = Espacio("Entrada", 1)

# Mostrar información inicial
print(g1)
print(g2)
print(g3)

# Probar acciones de gatos
print(g1.jugar(20, 10))
print(g2.alimentar(15, 20))

# Probar espacios
print(terraza.agregar_gato(g1))
print(terraza.agregar_gato(g2))
print(terraza.agregar_gato(g3)) 

print(terraza.mostrar_gatos())
print(entrada.mostrar_gatos())
