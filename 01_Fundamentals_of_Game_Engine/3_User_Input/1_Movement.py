# Movement and change of color of a rectangle in response to user
# input. Coordinates of rectangle shown in screen

import pygame
import sys
import random

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)

speed = 5

pygame.init()

FONT = pygame.font.SysFont("monospace", 24)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movement")

player = pygame.Rect(
    random.randint(40, SCREEN_WIDTH - 40),
    random.randint(40, SCREEN_HEIGHT - 40),
    40,
    40
)
player_color = WHITE

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                player.x = mouse_pos[0]
                player.y = mouse_pos[1]
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    running = False
                case pygame.K_c:
                    if player_color == WHITE:
                        player_color = GREEN
                    else:
                        player_color = WHITE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed

    if player.x < 0:
        player.x = 0
    if player.x > SCREEN_WIDTH - 40:
        player.x = SCREEN_WIDTH - 40
    if player.y < 0:
        player.y = 0
    if player.y > SCREEN_HEIGHT - 40:
        player.y = SCREEN_HEIGHT - 40

    screen.fill(BLACK)
    pygame.draw.rect(screen,player_color,player)
    pos_text = FONT.render(f"x: {player.x}, y: {player.y}", True, RED)
    screen.blit(pos_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()