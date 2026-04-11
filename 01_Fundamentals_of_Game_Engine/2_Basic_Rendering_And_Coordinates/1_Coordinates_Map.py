# Understanding coordinate system by drawing a dot in every corner
# and some distributed in the window

import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT =768

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RADIUS = 10

POS_0 = (0, 0)
POS_1 = (SCREEN_WIDTH, 0)
POS_2 = (0, SCREEN_HEIGHT)
POS_3 = (SCREEN_WIDTH, SCREEN_HEIGHT)
POS_4 = (SCREEN_WIDTH / 2, 0)
POS_5 = (SCREEN_WIDTH / 2, SCREEN_HEIGHT)
POS_6 = (0, SCREEN_HEIGHT / 2)
POS_7 = (SCREEN_WIDTH, SCREEN_HEIGHT / 2)
POS_8 = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coordinates Map")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill(BLACK)

    pygame.draw.circle(screen, WHITE, POS_0, RADIUS)
    pygame.draw.circle(screen, WHITE, POS_1, RADIUS)
    pygame.draw.circle(screen, WHITE, POS_2, RADIUS)
    pygame.draw.circle(screen, WHITE, POS_3, RADIUS)
    pygame.draw.circle(screen, WHITE, POS_4, RADIUS)
    pygame.draw.circle(screen, WHITE, POS_5, RADIUS)
    pygame.draw.circle(screen, WHITE, POS_6, RADIUS)
    pygame.draw.circle(screen, WHITE, POS_7, RADIUS)
    pygame.draw.circle(screen, WHITE, POS_8, RADIUS)

    pygame.display.flip()

pygame.quit()
sys.exit()