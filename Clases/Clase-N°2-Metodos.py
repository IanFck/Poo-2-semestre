class Fraccion ():

    def __init__ (self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador

    def __str__ (self):
        return f" {self.numerador}/{self.denominador}"
    
    def __add__(self, other):
        numerador = self.numerador * other.denominador + other.numerador * self.denominador
        denominador = self.denominador * other.denominador
        return Fraccion(numerador, denominador)
        

    def __mul__ (self, other):
        numerador = self.numerador * other.numerador
        denominador = self.denominador * other.denominador
        return Fraccion(numerador, denominador)

    def __eq__ (self, other):
        return f"{self.numerador * other.denominador} == {self. denominador * other.numerador}"

fraccion1 = Fraccion(1,5)
fraccion2 = Fraccion(4,6)

print ("Fraccion 1", fraccion1.__str__())
print ("Fraccion 2", fraccion2.__str__())
print ("Suma:", fraccion1+fraccion2)
print ("Multiplicacion", fraccion1 * fraccion2)
print ("Comparacion", fraccion1 == fraccion2)