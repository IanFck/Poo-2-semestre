# Los archivos tienen que estar en la mismas carpetas

import pygame 
from rectangulo_pequeno import RectanguloPequeno
from rectangulo_grande import RectanguloGrande

pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Colision Rectangular en Python")

background = (30,30,30)
color_colision = (234,63,63) # Color rojo

# Instanciasd de los rectangulos
rectangulo_pequeno = RectanguloPequeno(200,200,100,50)
rectangulo_grande = RectanguloGrande(400,300,150,100)

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    teclas = pygame.key.get_pressed()

    # Almacena la posicion actual de los rectangulos antes de moverlos
    pos_anterior_pequeno = rectangulo_pequeno.obtener_posicion()
    pos_anterior_grande = rectangulo_grande.obtener_posicion()

    rectangulo_pequeno.mover(teclas)
    rectangulo_grande.mover(teclas)

    if rectangulo_pequeno.Rect.colliderect(RectanguloGrande.rect):
        rectangulo_pequeno.restablecer_posicion(*pos_anterior_pequeno)
        rectangulo_grande.restablecer_posicion(*pos_anterior_grande)
        rectangulo_pequeno.cambiar_color(color_colision)
        rectangulo_grande.cambiar_color(color_colision)
    else:
        rectangulo_pequeno.cambiar_color((63,232,234))
        rectangulo_grande.cambiar_color((63,234,76))


    ventana.fill(background)
    rectangulo_pequeno.dibujar(ventana)
    rectangulo_grande.dibujar(ventana)

    pygame.display.update()

pygame.quit()
