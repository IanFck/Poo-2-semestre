# Empezamos importando la libreria pygame
import pygame as pg

# Inicializamos los modulos de la biblioteca pygame
pg.init()

# Aqui empezaremos a crear la ventana de nuestro juego
ventana = pg.display.set_mode((800,600))
pg.display.set_caption("Las Aventuras de Kroky")

# Aqui crearemos nuestro colores para el fondo del videojuego
Celeste = (140,200,255)
Verde_claro = (100,200,100)
Verde_oscuro = (40,100,40)

# Bucle para mantener el juego y poder salir
running = True 
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 

    # Cielo
    ventana.fill(Celeste)

    # Fondos del videojuego 
    pg.draw.rect(ventana, Celeste, (0, 0, 800, 400))       # cielo
    pg.draw.rect(ventana, Verde_claro, (0, 400, 800, 120)) # montaña
    pg.draw.rect(ventana, Verde_oscuro, (0, 520, 800, 80)) # bosque oscuro

    # Figura 
    vertices_triangulo =[(400,110), (350,200), (450,200)]
    pg.draw.polygon(ventana,(255,255,0),vertices_triangulo)
    
    #Comando para abrir la ventana
    pg.display.flip()