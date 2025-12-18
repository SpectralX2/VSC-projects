import pygame
from tiles import load_image, RED

IMG_ENEMY = "images/monsters/cyclops.png"
ENEMY_SPEED = 3
ENEMY_HP = 30

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = load_image(IMG_ENEMY, RED)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-10, -10)

        self.direction = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites
        
        self.speed = ENEMY_SPEED
        self.health = ENEMY_HP

    def get_player_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        
        distance = (player_vec - enemy_vec).magnitude()
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        return direction

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        for sprite in self.obstacle_sprites:
            if hasattr(sprite, 'hitbox') and sprite.hitbox.colliderect(self.hitbox):
                if direction == 'horizontal':
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                if direction == 'vertical':
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def update(self, player):
        dist = pygame.math.Vector2(self.rect.center).distance_to(player.rect.center)
        if dist < 500:
            self.direction = self.get_player_direction(player)
            self.move(self.speed)
        else:
            self.direction = pygame.math.Vector2()