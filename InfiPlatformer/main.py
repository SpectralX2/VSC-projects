import pygame
import sys
import random
from floatingPlatform import *
from player import *
from pygame.locals import *
 
pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Move the Square")
color = (90, 132, 185)
clock = pygame.time.Clock()
running = True
platforms = pygame.sprite.Group()
sprite_list = pygame.sprite.Group()
player = ""

def placeInitPlatforms():
    for y in range(height//100):
        for x in range(width//420):
            platform = FloatingPlatform((random.randint(64, int(width/1.2)), random.randint(0, int(height)-64)), "grassHalf.png", screen, 120, 120)
            platforms.add(platform)

def placePlayer(sprite_dict):
    global player
    player = Player((platforms.sprites()[-1].rect.centerx, platforms.sprites()[-1].rect.centery-300), sprite_dict)
    sprite_list.add(player)

def main():
    placeInitPlatforms()
    placePlayer(sprite_list)
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys [K_a]:
                player.left()
            if keys [K_d]:
                player.right()
        keys = pygame.key.get_pressed()
        screen.fill((color))
        player.update()
        sprite_list.draw(screen)
        platforms.draw(screen)
        pygame.display.flip()
main()