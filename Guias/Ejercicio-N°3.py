#Ejercicio 3 Guia de estudio N°1 Ian Fack
#Comenzaremos creando la clase Producto, dandole los atributos que nos pidieron
class Producto ():
    def __init__(self, nombre, precio : int, cantidad_disponible: int, SKU: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.SKU = SKU
        self.historial_de_cambios = [] 

#Para el metodo stock, le daremos un nuevo parametro llamado actualizacion donde lo sumaremos a la cantidad disponible
    def stock (self, actualizacion):
        self.cantidad_disponible += actualizacion
        self.historial_de_cambios.append(actualizacion) #Y aqui usamos append (comando para Lista), para agregar el cambio a la lista
        print(f"Actualizacion de stock {self.cantidad_disponible}")

#Para el metodo valor simplemente multiplicaremos el precio por la cantidad que esta dispolible
    def valor (self):
        productos_disponibles = self.precio * self.cantidad_disponible
        return f"Valor total de los productos disponibles ${productos_disponibles}"

    def __str__(self):
        return f"Estado actual del producto\n Producto: {self.nombre}, Precio: ${self.precio}, Cantidad Disponible: {self.cantidad_disponible}, SKU: {self.SKU}"
        

#Ahora les daremos datos a nuestras clases
Producto1 = Producto("Cuadernos",2500, 150, 143124)
Producto2 = Producto("Lapiz Pasta", 900, 84, 131344)
Producto3 = Producto("Corrector",540, 53, 123133)
Producto4 = Producto("Destacador",300, 75, 123131)

#Producto 1
print (f"{Producto1}")
print (f"{Producto1.valor()}")
Producto1.stock(10)
Producto1.stock(-5)
print(Producto1.valor())
print("Historial:", Producto1.historial_de_cambios)
print ("----------------------------------------")

#Producto 2
print (f"{Producto2}")
print (f"{Producto2.valor()}")
Producto2.stock(80)
Producto2.stock(-67)
print(Producto2.valor())
print("Historial:", Producto2.historial_de_cambios)


class Inventario ():
    def __init__(self):
        self.productos = {}

    def agregar_productos (self, producto):
        if producto.SKU in self.productos:
            print("El producto ya existe. Actualizando stock en vez de agregar.")
            self.productos[producto.SKU].stock(producto.cantidad_disponible)
        else:
            self.productos[producto.SKU] = producto

    def actualizar_stock(self, SKU, cambio):
        if SKU in self.productos:
            self.productos[SKU].stock(cambio)
        else:
            print("Producto no encontrado en el inventario")

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def valor_total_inventario(self):
        total = 0
        for producto in self.productos.values():
            total += producto.valor() 
        return total
    
Producto1 = Producto("Laptop", 1200, 5, "A001")
Producto2 = Producto("Mouse", 25, 50, "B002")
Producto3 = Producto("Teclado", 45, 30, "C003")

inventario = Inventario()

inventario.agregar_productos(Producto1)
inventario.agregar_productos(Producto2)
inventario.agregar_productos(Producto3)

inventario.mostrar_productos()

inventario.actualizar_stock("B002", 10)  
inventario.actualizar_stock("A001", -2)  

print("\n--- Después de actualizar stock ---")
inventario.mostrar_productos()

# Valor total del inventario
print("\nValor total del inventario:", inventario.valor_total_inventario())

