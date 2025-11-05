# Parcial N°1 
# Ian Fack

class Jugador:
    JUGADORES_CREADOS = 0
    POSICIONES_CREADAS= ["DEL","VOL","DEF","ARQ"]

    def __init__(self,nombre: str,edad : int, club:str):
        self.__nombre = nombre #Privado
        self.__edad = edad #Privado
        self.__posicion = [] #Privado
        self.goles = 0 #Publico
        self.club = club
        self.energia = [0,100]
        JUGADORES_CREADOS =+1 #Incrementados
        #Assert solicitados
        assert self.__posicion ("No puede estar vacia")
        assert self.__edad >=15
        assert 0<= self.energia <= 100
        assert self.goles >= 0
        assert club ("No puede estar vacio")

    @classmethod
    def creados(cls):
        return cls.JUGADORES_CREADOS

    @staticmethod 
    def posicion_valida(self):
        if self.posicion == "DEL":
            return True
        elif self.posicion == "VOL":
            return True
        elif self.posicion == "DEF":
            return True
        elif self.posicion == "ARQ":
            return True
        else:
            return False
            
    @property #Retorna nombre del jugador
    def nombre (self):
        return self.__nombre
    
    @property # Retorna edad del jugador
    def edad (self):
        return self.__edad
    
    @edad.setter
    def edad (self):
        if self.__edad >= 15:
            return print("Edad valida")
        else:
            print ("Edad no valida")

    @property #Retorna posición
    def posicion (self):
        return self.__posicion
    
    @property #Retorna la cantidad de goles
    def goles (self):
        return self.__goles
    
    def entrenar (min : int ,self):
        assert min>0 #A partir de 10 minutos se empezara a notar la disminucion de energia
        if min > 10:
            self.energia -= 10
        elif min > 50:
            self.energia -= 50
        elif min > 70:
            self.energia -= 70
        elif min > 90:
            self.energia -= 90
        elif min > 100:
            self.energia = 0
            return f"Energia acabada"
        else:
            return f"Los minutos ingresados son inferior a 0"
        
    def anotar_gol (self, goles_anotados:int):
        assert self.goles >= 0
        if goles_anotados == 1:
            self.goles += goles_anotados
        else:
            print("Error, debe ser mayor a 0")

    def __str__(self):
        return f"El jugador {self.__nombre} juega en el club:{self.club}, juega de {self.__posicion}, cuenta con energía {self.energia} y tiene la cantidad de {self.goles} goles"
    
Jugador1 = Jugador("Luis",20,"VOL", 1,"Deportes Castro", 100) 
Jugador2 = Jugador("Ian", 22,"DEF", 2, "Deportes Castro", 80)

print(Jugador1)
print(Jugador2)
Jugador1.anotar_gol(1)
Jugador2.anotar_gol(2)
Jugador1.entrenar(30)
Jugador2.entrenar(80)


