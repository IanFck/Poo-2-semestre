import pygame


class RectanguloPequeno:
    def __init__(self, x, y, ancho, alto):
        self.x= x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 1
        self.color = (63,232,234) # Color Verde
        self.rect = pygame.Rect(self.x,self.y,self.ancho, self.alto)


    def dibujar (self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)

    def mover(self, teclas):
        mov_x = 0
        mov_y = 0

        if teclas[pygame.K_LEFT]:
            mov_x = -1
        if teclas[pygame.K_RIGHT]:
            mov_x = 1
        if teclas[pygame.K_UP]:
            mov_y = -1
        if teclas[pygame.K_DOWN]:
            mov_y = 1

        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad 

    def restablecer_posicion(self, x, y):
        self.rect.x = x
        self.rect.y = y
    def obtener_posicion(self):
        return (self.rect.x, self.rect.y)
    
    def cambiar_color(self,color):
        self.color = color