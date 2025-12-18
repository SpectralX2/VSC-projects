import pygame
import os

TILESIZE = 32
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

IMG_WALL = "images/tiles/wall12.gif"
IMG_FLOOR = "images/tiles/floor13.gif"
IMG_DOOR_LOCKED = "images/tiles/door11.png"
IMG_DOOR_OPEN = "images/tiles/openDoor11.png"

def load_image(path, color_fallback):
    if path and os.path.exists(path):
        try:
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (TILESIZE, TILESIZE))
        except Exception:
            pass
    
    surf = pygame.Surface((TILESIZE, TILESIZE))
    surf.fill(color_fallback)
    return surf

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, is_wall=False, image_path=None):
        super().__init__(groups)
        self.image = load_image(image_path, BLUE if is_wall else (50, 50, 50))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

class Door(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = load_image(IMG_DOOR_LOCKED, (100, 0, 100))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.unlocked = False

    def unlock(self):
        if not self.unlocked:
            self.unlocked = True
            if os.path.exists(IMG_DOOR_OPEN):
                self.image = load_image(IMG_DOOR_OPEN, GREEN)
            else:
                self.image.fill(GREEN)

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, pos, groups, p_type):
        super().__init__(groups)
        self.p_type = p_type
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect(center=(pos[0] + TILESIZE//2, pos[1] + TILESIZE//2))

        if self.p_type == 'health':
            self.image.fill(RED)
        elif self.p_type == 'damage':
            self.image.fill((255, 215, 0))
        elif self.p_type == 'speed':
            self.image.fill((0, 255, 255))