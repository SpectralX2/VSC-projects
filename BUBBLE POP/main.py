import pygame, sys, random, math, os
from pygame.locals import *
from dot import *
from ball import *

pygame.init()
size = (width, height) = (400, 700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg_color = (0, 0, 0)
state = None

def image_path(name):
    return os.path.join("images", name)

ball_images = [
    image_path("sphere-04.png"),
    image_path("sphere-06.png"),
    image_path("sphere-07.png"),
    image_path("sphere-11.png"),
    image_path("sphere-12.png"),
    image_path("sphere-02.png")
]

big_font = pygame.font.SysFont("impact", 80)
sub_font = pygame.font.SysFont("impact", 30)

min_y = 10

def color_check(color, ball, balls, to_delete):
    ball.rect.x -= 2
    hit_list = pygame.sprite.spritecollide(ball, balls, False)
    ball.rect.x += 4
    hit_list += pygame.sprite.spritecollide(ball, balls, False)
    ball.rect.x -= 2
    for b in hit_list:
        if b.path == color and not to_delete.has(b):
            to_delete.add(b)
            if b is not ball:
                color_check(color, b, balls, to_delete)

def check_and_delete(ball, balls):
    to_delete = pygame.sprite.Group()
    color = ball.path
    color_check(color, ball, balls, to_delete)
    if len(to_delete) < 3:
        return
    for b in to_delete:
        b.kill()

def initialize(balls, dots, current_ball):
    global state, min_y
    state = "aiming"
    balls.empty()
    current_ball.empty()
    current_ball.add(Ball((183, 633), random.choice(ball_images)))
    for i in range(6):
        y = 10 + 30 * i
        if i % 2 == 0:
            for j in range(11):
                balls.add(Ball((7 + 34 * j, y), random.choice(ball_images)))
        else:
            for j in range(10):
                balls.add(Ball((24 + 34 * j, y), random.choice(ball_images)))
    min_y = 10
    if len(dots) == 0:
        for i in range(3):
            dots.add(AimingDot(30 + 35 * i))

def move_down(backboard, balls, line):
    global min_y, state
    min_y += 30
    backboard.y += 30
    for b in balls.sprites():
        b.rect.y += 30
        if b.rect.bottom > line.top:
            state = "game over"

def display_text(main_text, sub):
    text = big_font.render(main_text, True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    subtext = sub_font.render(sub, True, (255, 255, 255))
    subtext_rect = subtext.get_rect(midtop=(width // 2, text_rect.bottom))
    screen.blit(text, text_rect)
    screen.blit(subtext, subtext_rect)

def main():
    global screen, state
    dots = pygame.sprite.Group()
    backboard = pygame.Rect(0, 0, 400, 10)
    line = pygame.Rect(0, 600, 400, 10)
    current_ball = pygame.sprite.GroupSingle()
    balls = pygame.sprite.Group()
    initialize(balls, dots, current_ball)
    shot_count = 0

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
                elif event.key == K_SPACE:
                    if state == 'aiming':
                        state = 'fired'
                        angle = dots.sprites()[0].angle
                        print(f"Firing ball at angle: {angle}")
                        current_ball.sprite.set_speed(angle)
                    elif state in ["game over", "level cleared"]:
                        backboard.y = 0
                        shot_count = 0
                        initialize(balls, dots, current_ball)

        keys = pygame.key.get_pressed()
        if state == "aiming":
            if keys[K_RIGHT]:
                dots.update(1)
            if keys[K_LEFT]:
                dots.update(-1)

        if state == "fired":
            print("Ball is in motion")
            if current_ball.sprite.update(balls, backboard):
                print("Ball landed or collided")
                check_and_delete(current_ball.sprite, balls)
                if current_ball.sprite.rect.bottom > line.top:
                    state = "game over"
                elif len(balls) == 0:
                    state = "level cleared"
                else:
                    shot_count += 1
                    if shot_count % 2 == 0:
                        move_down(backboard, balls, line)
                    state = "aiming"
                    current_ball.add(Ball((183, 633), random.choice(ball_images)))

        screen.fill(bg_color)
        pygame.draw.rect(screen, (153, 0, 0), backboard)
        pygame.draw.rect(screen, (0, 77, 153), line)
        current_ball.draw(screen)
        balls.draw(screen)
        if state == "aiming":
            dots.draw(screen)
        elif state == "game over":
            display_text("Game over", "Press space to try again")
        elif state == "level cleared":
            display_text("You win!", "Press space to play again")
        pygame.display.flip()

if __name__ == "__main__":
    main()