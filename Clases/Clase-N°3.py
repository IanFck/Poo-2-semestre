import pygame as pg

pg.init()

ventana = pg.display.set_mode((800,600))
pg.display.set_caption("Figuras geometricas")

background_color = (0,0,0)

running = True 
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 

    ventana.fill(background_color)

    pg.darw.circle(ventana, (255,0,0), (400,300), 50)
    pg.darw.rect(ventana, (0,255,0), (150,200,100,50))
    pg.darw.line(ventana, (0,0,255), (100,100), (700,100),5)

    vertices_triangulo =[(400,110), (350,200), (450,200)]
    pg.draw.polygon(ventana,(255,255,0),vertices_triangulo)
    

