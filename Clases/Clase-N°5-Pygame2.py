import pygame as pg

# Inicio de la bilbioteca
pg.init()

# Seteo de la ventana #Setcaption nombre de la ventana
window = pg.display.set_mode ((800,600))
pg.display.set_caption("Conceptos Básicos")

# Color de fondo
background = (0,0,0) #Aqui ponemos el color de fondo con 

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    window.fill(background)

    # Dibujo de figuras
    pg.draw.circle(window, (255,255,0), (400,400), 20 )

    pg.display.update()

pg.quit()



