# Drawing 20 small points ("particles") radially distributed around
# a preset center location

import pygame
import sys
import math
import random

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

N_PARTICLES = 20
CENTER = (430, 325)
PARTICLE_RADIUS = 3

particles = []

for i in range(N_PARTICLES):
    angle = random.randint(0, 360)
    radius = random.randint(20, 100)
    x = CENTER[0] + radius * math.cos(math.radians(angle))
    y = CENTER[1] + radius * math.sin(math.radians(angle))
    particles.append((x, y))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Manual Particles")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    for particle in particles:
        pygame.draw.circle(screen, WHITE, particle, PARTICLE_RADIUS)
    pygame.display.flip()

pygame.quit()
sys.exit()