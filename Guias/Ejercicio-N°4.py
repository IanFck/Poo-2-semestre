class Pedido ():
    def __init__(self, numero_de_mesa):
        self.numero_de_mesa = numero_de_mesa
        self.lista = []
        self.total_del_pedido = 0.0

    def agregar_platos (self, nombre,precio:int):
        self.lista.append((nombre,precio))
        self.total_del_pedido += precio

    def total (self):
        return self.total_del_pedido
    
    def __len__(self):
        return len(self.lista)

    
    def __add__ (self, other):
        nuevo_pedido = Pedido(self.numero_de_mesa)
        nuevo_pedido.lista = self.lista + other.lista
        nuevo_pedido.total_del_pedido = self.total_del_pedido + other.total_del_pedido
        return nuevo_pedido

    def __del__(self):
        return f"El pedido {self.numero_de_mesa} ha sido completado"
    

Pedido1 = Pedido(3)
Pedido1.agregar_platos("Pizza",7500)
Pedido1.agregar_platos("Coca-Cola",1500)

Pedido2 = Pedido(3)
Pedido2.agregar_platos("Empanada de Queso", 2000)

print(f"Total del pedido 1: $ {Pedido1.total()}")
print(f"Numero de platos Pedido 1: {len(Pedido1)}")

Pedidos = Pedido1 + Pedido2
print(f"Total del pedido combinado: $ {Pedidos.total_del_pedido}")
print(f"Platos combinados: {Pedidos.lista}")