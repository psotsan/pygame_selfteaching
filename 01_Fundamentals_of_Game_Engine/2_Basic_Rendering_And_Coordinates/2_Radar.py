# Drawing a big circle (radar) and spawn random enemies within it

import pygame
import sys
import math
import random

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(0, 156, 255)

RADAR_RAD = 200
LINE_LENGTH = 300
LINE_WIDTH = 10
LINE1_END = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - LINE_LENGTH)
LINE2_END = (SCREEN_WIDTH / 2 + LINE_LENGTH, SCREEN_HEIGHT / 2)
LINE3_END = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + LINE_LENGTH)
LINE4_END = (SCREEN_WIDTH / 2 - LINE_LENGTH, SCREEN_HEIGHT / 2)

coords = []
enemy_size = 25
enemies = []

for i in range(3):
    distance = RADAR_RAD + 10
    while distance > RADAR_RAD:
        pos_x = random.randint(0, SCREEN_WIDTH)
        pos_y = random.randint(0, SCREEN_HEIGHT)
        distance = math.sqrt((SCREEN_CENTER[0] - pos_x) ** 2 + (SCREEN_CENTER[1] - pos_y) ** 2)

    coords.append((pos_x, pos_y))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Radar")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLACK)
    pygame.draw.circle(screen, BLUE, SCREEN_CENTER, RADAR_RAD)
    pygame.draw.line(screen, BLUE, SCREEN_CENTER, LINE1_END, LINE_WIDTH)
    pygame.draw.line(screen, BLUE, SCREEN_CENTER, LINE2_END, LINE_WIDTH)
    pygame.draw.line(screen, BLUE, SCREEN_CENTER, LINE3_END, LINE_WIDTH)
    pygame.draw.line(screen, BLUE, SCREEN_CENTER, LINE4_END, LINE_WIDTH)
    for coord in coords:
        enemy = pygame.Rect(coord[0],coord[1], enemy_size, enemy_size)
        pygame.draw.rect(screen, WHITE, enemy)
    pygame.display.flip()

pygame.quit()
sys.exit()
