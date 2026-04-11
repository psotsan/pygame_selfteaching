# Changing window background color in response to keyboard events

import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

RED = (255, 0, 0)
BLUE = (20, 20, 80)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Keyboard Events")

running = True

screen.fill(BLUE)
pygame.display.flip()

# Main loop
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    running = False
                case pygame.K_f:
                    screen.fill(RED)
                    pygame.display.set_caption("Keyboard Events - Red bg")
                case pygame.K_n:
                    screen.fill(BLUE)
                    pygame.display.set_caption("Keyboard Events - Blue bg")
    # Status
    pass

    # Render
    pygame.display.flip()

pygame.quit()
sys.exit()