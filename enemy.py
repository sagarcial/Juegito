import pygame, random
from global_Var import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("img/enemy.png")
        original_image.set_colorkey(black)
        self.image = pygame.transform.scale(original_image, (80, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1,5)
        self.speed_x = random.randrange(-5,5)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width +25:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1,10)