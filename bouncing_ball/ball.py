import pygame, random

class Ball(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load("ball.png")
        scale = random.randint(1,5)*10
        self.image = pygame.transform.smoothscale(self.image, (scale,scale))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, random.randint(2,5))
        self.speed.rotate_ip(random.randint(0,360))
    
    def update(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 :
            self.speed[0] *= -1
            self.rect.left = 0
        if self.rect.right > screen_info.current_w:
                self.speed[0] *= -1
                self.rect.right = screen_info.current_w
        if self.rect.top < 0 :
            self.speed[1] *= -1
            self.rect.top = 0
        if self.rect.bottom > screen_info.current_h:
             self.speed[1] *= -1
             self.rect.bottom = screen_info.current_h