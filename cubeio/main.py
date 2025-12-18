import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

FPS = 10
clock = pygame.time.Clock()

def draw_glow(surface, color, pos, max_radius):
    for i in range(max_radius, 0, -4):
        alpha = max(0, 50 - (50 * i // max_radius))
        glow_surf = pygame.Surface((i*2, i*2), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (*color, alpha), (i, i), i)
        surface.blit(glow_surf, (pos[0]-i + 10, pos[1]-i + 10))

def rainbow_color(offset, speed=0.002):
    import math, time
    t = time.time() + offset
    r = int((math.sin(t*speed) + 1) * 127)
    g = int((math.sin(t*speed + 2) + 1) * 127)
    b = int((math.sin(t*speed + 4) + 1) * 127)
    return (r, g, b)

class Player:
    def __init__(self):
        self.size = 20
        self.body = [[WIDTH//2, HEIGHT//2]]
        self.dir = (0, 0)

    def move(self):
        dx, dy = self.dir
        if dx != 0 or dy != 0:
            new_head = [self.body[0][0] + dx*self.size, self.body[0][1] + dy*self.size]
            new_head[0] %= WIDTH
            new_head[1] %= HEIGHT
            self.body.insert(0, new_head)
            self.body.pop()

    def grow(self):
        self.body.append(self.body[-1][:])

    def shrink(self):
        if len(self.body) > 1:
            self.body.pop()

    def draw(self, win):
        for segment in self.body:
            draw_glow(win, (50, 50, 255), segment, 30)
            pygame.draw.rect(win, BLACK, (segment[0], segment[1], self.size, self.size))

class Food:
    def __init__(self, color):
        self.size = 20
        self.color = color
        self.spawn()

    def spawn(self):
        self.x = random.randrange(0, WIDTH - self.size, self.size)
        self.y = random.randrange(0, HEIGHT - self.size, self.size)

    def draw(self, win):
        glow_color = (0, 255, 0) if self.color == GREEN else (255, 0, 0)
        draw_glow(win, glow_color, [self.x, self.y], 25)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

def main():
    run = True
    player = Player()
    good_food = Food(GREEN)
    bad_food = Food(RED)
    level = 1
    good_food_eaten = 0
    bad_foods = [Food(RED)]

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.dir != (1, 0):
            player.dir = (-1, 0)
        if keys[pygame.K_RIGHT] and player.dir != (-1, 0):
            player.dir = (1, 0)
        if keys[pygame.K_UP] and player.dir != (0, 1):
            player.dir = (0, -1)
        if keys[pygame.K_DOWN] and player.dir != (0, -1):
            player.dir = (0, 1)

        player.move()

        head_rect = pygame.Rect(player.body[0][0], player.body[0][1], player.size, player.size)

        if head_rect.colliderect(pygame.Rect(good_food.x, good_food.y, good_food.size, good_food.size)):
            player.grow()
            good_food.spawn()
            good_food_eaten += 1

            if good_food_eaten % 5 == 0:
                level += 1
                bad_foods.append(Food(RED))
        
        for bad_food in bad_foods:
            if head_rect.colliderect(pygame.Rect(bad_food.x, bad_food.y, bad_food.size, bad_food.size)):
                player.shrink()
                bad_food.spawn()

        for y in range(0, HEIGHT, 4):
            color = rainbow_color(y)
            pygame.draw.rect(WIN, color, (0, y, WIDTH, 4))
        player.draw(WIN)
        good_food.draw(WIN)
        bad_food.draw(WIN)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
