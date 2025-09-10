class Libro ():
    def __init__(self, titulo,autor,anio_de_publicacion:int,stock:int):
        self.titulo = titulo
        self.autor = autor
        self.anio_de_publicacion = anio_de_publicacion
        self.stock = stock

    def __str__ (self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año de publicacion: {self.anio_de_publicacion}, Stock: {self.stock}"
    

class Biblioteca ():
    def __init__(self):
        self.libros = {}

    def agregar_libro (self, libro):
        if libro.titulo in self.libros:
            self.libros[libro.titulo].stock += libro.stock
        else:
            self.libros[libro.titulo] = libro

    def buscar_libro (self, titulo):
        if titulo in self.libros:
            return self.libros[titulo]
        else:
            return None
        
    def actualizar_libro(self, titulo, autor=None, anio=None, cantidad=None):
        libro = self.buscar_libro(titulo)
        if libro:
            if autor is not None:
                libro.autor = autor
            if anio is not None:
                libro.anio_publicacion = anio
            if cantidad is not None:
                libro.stock = cantidad
            return True
        return False
        
Biblioteca = Biblioteca()

Libro1 = Libro("Papelucho","Marcela Paz",1947,250)
Libro2 = Libro("Harry Potter", "J. K. Rowling",1997, 187)

Biblioteca.agregar_libro(Libro1)
Biblioteca.agregar_libro(Libro2)

buscadoH = Biblioteca.buscar_libro("Harry Potter")
if buscadoH:
    print(buscadoH.__str__())

Biblioteca.actualizar_libro("Harry Potter", cantidad=190)
print(Biblioteca.buscar_libro("Harry Potter").__str__())

BuscadoP = Biblioteca.buscar_libro("Papelucho")
if BuscadoP:
    print(BuscadoP.__str__())

Biblioteca.actualizar_libro("Papelucho", cantidad=300)
print(Biblioteca.buscar_libro("Papelucho").__str__())