import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image_path):
        self.image = pygame.image.load("p1_jump.png")
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.momentum = pygame.math.Vector2(0, 0)
        self.facing = "r"

def update(self):
    self.image = self.sprite_dict['p1_jump']
    if self.facing == "l":
        self.image = pygame.transform.flip(self.image, True, False)