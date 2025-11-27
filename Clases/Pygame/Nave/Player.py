# Importamos la libreria Pygame
import pygame

# Y conectamos settings cpn las variables de clase que queremos ocupar
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED

# Aqui hereda la biblioteca Pygame heredando el modulo sprite y dentro la clase Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Atributos de la nave
        self.image = pygame.surface((50,50),pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2 # Aparecera al medio de la pantalla
        self.rect.bottom = SCREEN_HEIGHT - 10

        # Dibujar el triangulo
        pygame.draw.polygon(self.image, (0,0,255), [(25,0),(0,50),(50,50)])

    def update(self):
        keys = pygame.key.get_pressed()
        
        # Teclas ocupadas
        if keys [pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys [pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Mantener la nave dentro de los limites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        