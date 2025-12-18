import pygame
import random

class FloatingPlatform(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_path, screen, width=120, height=120):
        super().__init__()
        self.image = pygame.image.load(sprite_path)

        pygame.transform.scale(self.image, [width,height])
        self.image.blit(self.image, (0,0))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = pos