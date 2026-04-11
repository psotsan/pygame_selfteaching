# Drawing a simple window with its caption, defining its dimensions,
# background color and implementing simple game loop

import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Functional Screen")

running = True

# Main loop
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Status
    pass

    # Render
    screen.fill((20, 20, 80))
    pygame.display.flip()

pygame.quit()
sys.exit()