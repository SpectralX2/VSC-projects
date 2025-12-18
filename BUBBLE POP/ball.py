import pygame, math

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, img_path):
        super().__init__()
        self.path = img_path
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.smoothscale(self.image, (34, 34))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.speed = [0, 0]

    def check_off_screen(self):
        if self.rect.x < 0:
            self.rect.x += 34
        elif self.rect.right > 400:
            self.rect.x -= 34

    def update(self, balls, backboard):
        print(f"Ball pos: {self.rect.center}, speed: {self.speed}")
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.center = (self.x, self.y)

        if self.rect.left < 0:
            print("Bounce left wall")
            self.rect.left = 0
            self.speed[0] *= -1
        elif self.rect.right > 400:
            print("Bounce right wall")
            self.rect.right = 400
            self.speed[0] *= -1

        hit_list = pygame.sprite.spritecollide(self, balls, False)
        print(f"Hit count: {len(hit_list)}")
        if hit_list:
            for b in hit_list:
                if pygame.sprite.collide_circle(self, b):
                    balls.add(self)
                if self.rect.y > b.rect.y + 16:
                    self.rect.y = b.rect.y + 30
                else:
                    self.rect.y = b.rect.y
                if self.rect.centerx > b.rect.centerx:
                    self.rect.x = b.rect.x + (17 if self.rect.y != b.rect.y else 34)
                else:
                    self.rect.x = b.rect.x - (17 if self.rect.y != b.rect.y else 34)
                self.speed = [0, 0]
                self.check_off_screen()
                return True

        if self.rect.colliderect(backboard):
            print("Hit backboard")
            self.rect.y = backboard.bottom
            self.rect.x = 7 + 34 * round((self.x - 7) / 34)
            balls.add(self)
            self.check_off_screen()
            return True

        return False

    def set_speed(self, angle):
        angle = math.radians(angle)
        dx = math.cos(angle) * 3  # Reduced from 5
        dy = math.sin(angle) * 3
        self.speed = [dx, dy]
