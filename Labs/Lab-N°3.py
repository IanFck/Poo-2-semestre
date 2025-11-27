# Lab N°3 Ian Fack

# A. La Clase Base Principal
class Contenido ():
    # Atributos: titulo(str), anio(int).
    def __init__(self, titulo:str, anio:int):
        self.titulo = titulo
        self.anio = anio

    # Método: mostrar_detalle(): Imprime el título y el año
    def mostrar_detalle(self):
        return f"{self.titulo} del año {self.anio}"
    
# B. Estructuras de Clases
class Reproducible():
    def reproducir (self):
        return f"Reproduciendo {self.titulo}"
        

class Calificable ():
    def __init__(self, rating: float):
        self.rating = rating
        
    def calificar (self):
        return f"Actualizando rating y imprimiendo nueva calificación {self.rating}"
    


# C. Subclases
class Película (Contenido, Reproducible):
    def __init__(self, titulo, anio, duracion_minutos: int):
        self.duracion_minutos = duracion_minutos
        super().__init__(titulo, anio)


class Documental (Contenido):
    def __init__(self,titulo, anio, tema:str):
        self.tema = tema 
        super().__init__(titulo, anio)

    def lista_de_reproduccion (self):
        return f"{self.titulo}, {self.anio}, {self.tema}"
    
class Miniserie(Contenido, Reproducible, Calificable):
    def __init__(self, titulo, anio, rating, num_episodios:int):
        self.num_episodios = num_episodios
        super().__init__(titulo, anio)
    
    def ejecutar_accion (self):
        return f"{self.reproducir()} y {self.mostrar_detalle()}"
    
lista_mixta = [Película, Miniserie, Documental]
    

    
# Objetos
# Pelicula
Peli = Película ("Cars", 2003, 240)
print(Peli.reproducir())

print("------------------------------")

# Documental
Documental1 = Documental ("Avenida Brasil", 2016, "Accion y suspenso")
print(Documental1.lista_de_reproduccion())
print("-------------------------------")

# Miniserie
Serie = Miniserie ("El juego del calamar",2020, 9.8, 240)
print(Serie.reproducir())
print(Serie.mostrar_detalle())
#print(Serie.calificar())




