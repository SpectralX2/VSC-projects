import pygame
import random
import math
import sys
from pygame.locals import *
from cat import *


pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w,screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (100,0,150)

cat_images = []

#def get_images():
    #cat_sheet = SpriteSheet('images/runningcat.png')
    #for i in range(4):
    #    for j in range(2):
    #        cat_images.append(cat_sheet.get_image(j*512,i*256,512,256))
    #        cat_images[-1] = pygame.transform.smoothscale(cat_images[-1],(180,90))

def create_background():
    background = pygame.Surface((width,height))
    bg_img = pygame.image.load("images/ground0.gif")
    for i in range(math.ceil(width/32)):
        for j in range(math.ceil(height/32)):
            background.blit(bg_img,(i*32,j*32))
    return background

def main():
    #get_images()
    #cat = Cat((-90,random.randint(50,height-50)),cat_images)
    backgound = create_background()
    #cat_image = cat_images[0]
    #cat_rect = cat_image.get_rect()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        frame = pygame.time.get_ticks() // 60 % 8
        #cat.update()
        screen.blit(backgound,(0,0))
        #cat.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()

