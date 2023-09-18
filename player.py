import pygame
from global_Var import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("img/player.png")
        original_image.set_colorkey(black)
        self.image = pygame.transform.scale(original_image, (70, 100))  # Ajusta el tamaño del sprite aquí
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10
        self.speed = 0

    def update(self):
        self.rect.x += self.speed

        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

    def move_left(self):
        self.speed = -5

    def move_right(self):
        self.speed = 5

    def stop(self):
        self.speed = 0