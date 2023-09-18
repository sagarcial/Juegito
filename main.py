import pygame
from player import *
from enemy import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Camino Hacia El Anillo")
clock = pygame.time.Clock()

fps = 60 

all_sprites = pygame.sprite.Group() 
all_enemys = pygame.sprite.Group() 

player = Player()
all_sprites.add(player)

for i in range(4):
    enemy = Enemy()
    all_sprites.add(enemy)
    all_enemys.add(enemy)

running = True

while running: #Funcion de la movilidad de la nave
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()

        elif event.type == pygame.KEYUP: #Para que no se mueva infinitamente
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

    all_sprites.update()
    screen.fill(black)

    all_sprites.draw(screen)

    pygame.display.flip()
