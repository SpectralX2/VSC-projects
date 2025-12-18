import pygame
from tiles import load_image, GREEN, WHITE

IMG_PLAYER = "images/player/human.png"
PLAYER_START_HP = 100
PLAYER_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = load_image(IMG_PLAYER, GREEN)
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-10, -10)

        self.direction = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites
        
        self.speed = PLAYER_SPEED
        self.health = PLAYER_START_HP
        self.max_health = PLAYER_START_HP
        self.damage = 10
        self.score = 0
        
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = 0
        self.attack_hit_done = False

    def input(self):
        if self.attacking:
            return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE]:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.attack_hit_done = False
            self.perform_attack()

    def perform_attack(self):
        self.image = self.original_image.copy()
        self.image.fill(WHITE, special_flags=pygame.BLEND_RGB_ADD)

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

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.image = self.original_image

    def update(self):
        self.input()
        self.cooldowns()
        self.move(self.speed)