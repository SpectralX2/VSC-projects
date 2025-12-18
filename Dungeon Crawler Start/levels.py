import pygame
import random
from tiles import Tile, Door, PowerUp, TILESIZE, IMG_WALL, IMG_FLOOR
from player import Player
from enemy import Enemy

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.item_sprites = pygame.sprite.Group()
        
        self.player = None
        self.exit_door = None
        self.level_count = 1

    def create_map(self):
        self.visible_sprites.empty()
        self.obstacle_sprites.empty()
        self.enemy_sprites.empty()
        self.item_sprites.empty()

        WIDTH_TILES = 60
        HEIGHT_TILES = 60
        
        grid = [['w' for _ in range(WIDTH_TILES)] for _ in range(HEIGHT_TILES)]
        
        floor_count = 0
        max_floors = 600 + (self.level_count * 50)
        
        x, y = WIDTH_TILES // 2, HEIGHT_TILES // 2
        floors = []
        
        while floor_count < max_floors:
            if grid[y][x] != 'f':
                grid[y][x] = 'f'
                floors.append((x, y))
                floor_count += 1
            
            direction = random.randint(1, 4)
            if direction == 1 and x > 2:
                x -= 1
            elif direction == 2 and x < WIDTH_TILES - 3:
                x += 1
            elif direction == 3 and y > 2:
                y -= 1
            elif direction == 4 and y < HEIGHT_TILES - 3:
                y += 1

        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                pos = (col_idx * TILESIZE, row_idx * TILESIZE)
                if cell == 'w':
                    Tile(pos, [self.visible_sprites, self.obstacle_sprites], is_wall=True, image_path=IMG_WALL)
                else:
                    Tile(pos, [self.visible_sprites], is_wall=False, image_path=IMG_FLOOR)

        start_pos = (floors[0][0] * TILESIZE, floors[0][1] * TILESIZE)
        self.player = Player(start_pos, [self.visible_sprites], self.obstacle_sprites)

        end_pos = (floors[-1][0] * TILESIZE, floors[-1][1] * TILESIZE)
        self.exit_door = Door(end_pos, [self.visible_sprites, self.obstacle_sprites])

        possible_spawns = floors[1:-1]
        
        for _ in range(10 + self.level_count * 2):
            if not possible_spawns:
                break
            coord = random.choice(possible_spawns)
            pos = (coord[0] * TILESIZE, coord[1] * TILESIZE)
            Enemy(pos, [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites)
            
        for _ in range(5 + self.level_count):
            if not possible_spawns:
                break
            coord = random.choice(possible_spawns)
            pos = (coord[0] * TILESIZE, coord[1] * TILESIZE)
            
            r = random.random()
            if r < 0.6:
                p_type = 'health'
            elif r < 0.8:
                p_type = 'damage'
            else:
                p_type = 'speed'
            
            PowerUp(pos, [self.visible_sprites, self.item_sprites], p_type)

    def run(self):
        self.player.update()
        self.enemy_sprites.update(self.player)
        self.item_sprites.update()
        
        self.visible_sprites.custom_draw(self.player)
        
        if self.player.attacking and not self.player.attack_hit_done:
            self.player.attack_hit_done = True
            attack_rect = self.player.rect.inflate(40, 40)
            hit_enemies = [e for e in self.enemy_sprites if attack_rect.colliderect(e.rect)]
            for enemy in hit_enemies:
                enemy.take_damage(self.player.damage)
                vec = pygame.math.Vector2(enemy.rect.center) - pygame.math.Vector2(self.player.rect.center)
                if vec.length() > 0:
                    vec = vec.normalize()
                    enemy.hitbox.x += vec.x * 20
                    enemy.hitbox.y += vec.y * 20
                    enemy.rect.center = enemy.hitbox.center

        for enemy in self.enemy_sprites:
            if enemy.hitbox.colliderect(self.player.hitbox):
                self.player.health -= 0.5

        hit_items = pygame.sprite.spritecollide(self.player, self.item_sprites, True)
        for item in hit_items:
            if item.p_type == 'health':
                self.player.health = min(self.player.health + 25, self.player.max_health)
            elif item.p_type == 'damage':
                self.player.damage += 5
            elif item.p_type == 'speed':
                self.player.speed += 1

        dist_to_door = pygame.math.Vector2(self.player.rect.center).distance_to(self.exit_door.rect.center)
        if dist_to_door < 50:
            self.exit_door.unlock()
            if self.player.rect.colliderect(self.exit_door.rect):
                self.level_count += 1
                self.create_map()