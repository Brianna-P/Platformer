import pygame, sys
from level import Level
from settings import *

#setup
pygame.init()
#pygame.mixer.init()
screen_width, screen_height = 1200, screen_height
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)



