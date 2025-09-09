class Prodcuto ():
    def __init__(self, nombre, precio : int, cantidad_disponible, SKU, historial_de_cambios):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.SKU = SKU
        self.historial_de_cambios = []

    def stock (self, SKU):
        