class Cancion():
    def __init__ (self, titulo, artista, duracion_segundos : int):
        self.titulo = titulo 
        self.artista = artista
        self.duracion_segundos = duracion_segundos

def milissegundos(self):
    m, s = divmod(max(self.duracion_segundos(),0), 60)
    return f"({m}:{s})"

def __str__(self):
    return f"{self.titulo} - {self.artista} {self.duracion_segundos}"



class Playlist():
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_de_canciones = []


def agregar (self, Cancion):
    self.lista_de_canciones.append(Cancion)

def duracion_total (self):
    return sum(c.duracion_segundos for c in self.canciones)

def milissegundos_total(self):
    total = self.duracion_total()
    m,s = divmod(max(total(),0), 60)
    return f"({m}:{s})"


def __len__(self):
    return len(self.lista_de_canciones)

def __add__(self, other):
    nueva = Playlist(f"{self.nombre} + {other.nombre}")

    nueva.lista_de_canciones = self.lista_de_canciones + other.lista_de_canciones
    return nueva

def __str__(self):
    encabezado = f"Playlist: {self.nombre},| X canciones {len(self.lista_de_canciones)} | Total: {self.milisegundos_total()}"

    if not self.lista_de_canciones:
        return encabezado, f"Lista Vacia"
    
    lineas = [encabezado]
    
    for i, c in enumerate(self.lista_de_canciones):
        lineas.append(f"{i} : {c}")
    return "\n". join(lineas)

    
