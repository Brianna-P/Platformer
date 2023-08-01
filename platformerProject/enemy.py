import pygame
from settings import tile_size

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.original_x = self.rect.x
        self.directional = 1
        self.distance = tile_size * 2


    def move(self):
        traversal = self.original_x + self.distance
        if self.rect.x != traversal:
            #dx = self.rect.x - traversal
            self.rect.x += traversal/traversal
        else:
            self.distance *= -1
            
    
    
 #   def attack(self, player):
#       if distance <= self.attack_radius:
 #           ???ATATACK

    def update(self):
       #self.move()
        pass