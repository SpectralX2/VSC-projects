import pygame, random, sys
from pygame.locals import *

pygame.init()

size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (26, 255, 255)

ball1_image = pygame.image.load("ball.png").convert_alpha()
scale1 = random.randint(2, 6) * 10
ball1_image = pygame.transform.smoothscale(ball1_image, (scale1, scale1))
ball1_rect = ball1_image.get_rect(center=(width//2, height//2))
ball1_speed = pygame.math.Vector2(0, random.randint(2, 5))
ball1_speed.rotate_ip(random.randint(0, 360))

ball2_image = pygame.image.load("ball2.png").convert_alpha()
scale2 = random.randint(2, 6) * 10
ball2_image = pygame.transform.smoothscale(ball2_image, (scale2, scale2))
ball2_rect = ball2_image.get_rect(center=(width//3, height//3))
ball2_speed = pygame.math.Vector2(0, random.randint(2, 5))
ball2_speed.rotate_ip(random.randint(0, 360))

running = True
while running:
    event = pygame.event.poll()
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

    clock.tick(60)
    screen.fill(color)

    ball1_rect.center += ball1_speed
    if ball1_rect.left <= 0 or ball1_rect.right >= width:
        ball1_speed.x *= -1
    if ball1_rect.top <= 0 or ball1_rect.bottom >= height:
        ball1_speed.y *= -1
    screen.blit(ball1_image, ball1_rect)

    ball2_rect.center += ball2_speed
    if ball2_rect.left <= 0 or ball2_rect.right >= width:
        ball2_speed.x *= -1
    if ball2_rect.top <= 0 or ball2_rect.bottom >= height:
        ball2_speed.y *= -1
    screen.blit(ball2_image, ball2_rect)

    pygame.display.flip()
