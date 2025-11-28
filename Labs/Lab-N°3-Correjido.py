# A. Clase Base
class Contenido:
    def __init__(self, titulo: str, anio: int):
        self.titulo = titulo
        self.anio = anio

    def mostrar_detalle(self):
        return f"{self.titulo} del año {self.anio}"
    
class Reproducible:
    """Interfaz de reproducción: debe ser implementada por subclases."""
    def reproducir(self):
        raise NotImplementedError("La subclase debe implementar este método.")


class Calificable:
    def __init__(self):
        self.rating = 0.0

    def calificar(self, puntuacion: float):
        self.rating = puntuacion
        return f"Nuevo rating: {self.rating}"
    
class Pelicula(Contenido, Reproducible):
    def __init__(self, titulo, anio, duracion_minutos: int):
        super().__init__(titulo, anio)
        self.duracion_minutos = duracion_minutos

    def reproducir(self):
        return f"Reproduciendo película '{self.titulo}' ({self.duracion_minutos} min)"


class Documental(Contenido):
    def __init__(self, titulo, anio, tema: str):
        super().__init__(titulo, anio)
        self.tema = tema

    def lista_de_reproduccion(self):
        return f"{self.titulo} ({self.anio}) - Tema: {self.tema}"


class Miniserie(Contenido, Reproducible, Calificable):
    def __init__(self, titulo, anio, num_episodios: int):
        Contenido.__init__(self, titulo, anio)
        Calificable.__init__(self)    # Inicializa rating
        self.num_episodios = num_episodios

    def reproducir(self):
        return f"Reproduciendo miniserie '{self.titulo}' ({self.num_episodios} episodios)"

    def ejecutar_accion(self):
        return f"{self.reproducir()} | {self.mostrar_detalle()}"


def lista_de_reproduccion(lista_contenidos):
    print("=== Lista de Reproducción ===")
    for contenido in lista_contenidos:
        if hasattr(contenido, "reproducir"):   # Duck typing
            print(contenido.reproducir())
        else:
            print(f"No se puede reproducir: {contenido.titulo}")
    print("---------------------------------")

if __name__ == "__main__":

    # Película
    peli = Pelicula("Cars", 2003, 240)

    # Documental
    doc = Documental("Avenida Brasil", 2016, "Acción y Suspenso")

    # Miniserie
    mini = Miniserie("El juego del calamar", 2020, 9)

    # Prueba LSP
    lista_mixta = [peli, doc, mini]
    lista_de_reproduccion(lista_mixta)

    # Prueba Herencia Múltiple y Polimorfismo
    print(mini.reproducir())
    print(mini.mostrar_detalle())
    print(mini.calificar(9.8))