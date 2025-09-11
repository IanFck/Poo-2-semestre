#Ejercicio 1 Guia de Estudio N°1 Ian Fack 
#Creamos la clase ReservaHostal(), poniendo los atributos pedidos, con el detalle de poner las fechas en Int, para poder calcular despues la duracion de la estadias
class ReservaHostal ():
    def __init__(self, nombre_del_cliente, fecha_de_entrada: int, fecha_de_salida: int, numero_de_habitacion):
        self.nombre_del_cliente = nombre_del_cliente
        self.fechaE = fecha_de_entrada
        self.fechaS = fecha_de_salida
        self.numero_de_habitacion = numero_de_habitacion

    #Un método para calcular la duración de la estadía del cliente.
    #Para calcular, solo simplemente restamos la salida con la entrada
    def duracion (self):
        estadia = self.fechaS - self.fechaE
        return f"{estadia} dias"
    
    #Un método mágico para mostrar la información de la reserva.
    def __str__ (self):
        return f"{self.nombre_del_cliente}, Fecha de entrada: {self.fechaE} de Septiembre, Fecha de salida: {self.fechaS} de Septiembre, Numero de habitación: N°{self.numero_de_habitacion}"

    #Un método para cambiar la fecha de salida.
    #Aqui creamos una nueva variable nueva_fecha dandole tambien self.fechaS
    def cambio_de_fecha (self, nueva_fecha):
        self.fechaS = nueva_fecha
        return f"{nueva_fecha}"
    

#Le damos datos a nuestras clase
Reserva1 = ReservaHostal("Ian Fack", 4, 7, 5)
Reserva2 = ReservaHostal("Alejandro Fernandez", 5, 7, 10)
Reserva3 = ReservaHostal("Josefina Castro", 8, 14, 11)
Reserva4 = ReservaHostal("Valentina Pineda", 17, 30, 20)

# Se debe eliminar un objeto ReservaHostal, además de imprimir un mensaje indicando que la reserva ha sido cancelada.
print (F"La Reserva de: {Reserva2.nombre_del_cliente} ha sido cancelada")
del Reserva2
print ("-----------------------------------------------------------")
#Aqui imprimimos nuestro datos 

#Datos de la reserva 1
print("Reserva 1")
print (f"La reserva 1 es de: {Reserva1}")
#Duracion de la reserva 1
print (f"Se quedara durante {Reserva1.duracion()}")
#Cambio de fecha
print (f"La persona {Reserva1.nombre_del_cliente} cambio su Fecha de salida!")
#Hasta cuando se queda
print (f"La nueva fecha de salida es el: {Reserva1.cambio_de_fecha(10)} de Septiembre")

print ("-----------------------------------------------------------")
#Datos de la reserva 3
print ("Reserva 3")
print (f"La reserva 1 es de: {Reserva3}")
print (f"Se quedara durante {Reserva3.duracion()}")
print (f"La persona {Reserva3.nombre_del_cliente} cambio su Fecha de salida!")
print (f"La nueva fecha de salida es el: {Reserva3.cambio_de_fecha(16)} de Septiembre")

print ("-----------------------------------------------------------")
#Datos de la reserva 4
print ("Reserva 4")
print (f"La reserva 1 es de: {Reserva4}")
print (f"Se quedara durante {Reserva4.duracion()}")
print (f"La persona {Reserva4.nombre_del_cliente} cambio su Fecha de salida!")
print (f"La nueva fecha de salida es el: {Reserva4.cambio_de_fecha(31)} de Septiembre")



