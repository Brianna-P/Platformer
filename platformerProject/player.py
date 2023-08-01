import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)

        #movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.gravity = 0.8
        self.jump_speed = -12
        self.previously_jumped = True


 #   def import_character_assets(self);
  #      character_path = 
   #     self.animations = 
#
 #       for animation in self.animations.keys():
  #          full_path = character_path + animation
   #         self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if not self.previously_jumped:
                self.jump()
                self.previously_jumped = True
            if self.direction.y == 0:
                self.previously_jumped = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        #if self.jumpable:
        self.direction.y = self.jump_speed
        #if self.direction.y == 0:
            #self.jumpable = True
        #else:
            #self.jumpable = False

    def update(self):
    #    self.rect.x += self.direction.x * self.speed
        self.get_input()
        
