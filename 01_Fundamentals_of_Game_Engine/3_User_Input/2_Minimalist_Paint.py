# A minimalist paint application. +, - change brush size. 1, 2, 3
# change color. R clears the screen

import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(0, 0, 255)
RED = pygame.Color(255, 0, 0)

clock = pygame.time.Clock()
color = BLACK
radius = 6

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minimalist Paint")

running = True
screen.fill(WHITE)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    running = False
                case pygame.K_r:
                    screen.fill(WHITE)
                case pygame.K_1:
                    color = BLACK
                case pygame.K_2:
                    color = RED
                case pygame.K_3:
                    color = BLUE
                case pygame.K_PLUS:
                    radius = radius + 2 if radius < 40 else 40
                case pygame .K_MINUS:
                    radius = radius - 2 if radius > 2 else 2

    if pygame.mouse.get_pressed()[0]:
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), radius)
    pygame.display.flip()

pygame.quit()
sys.exit()