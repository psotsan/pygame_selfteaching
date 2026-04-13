import pygame
import sys
import os
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED, INITIAL_BALL_SPEED,
    PLAYER_WIDTH, PLAYER_HEIGHT, BALL_RADIUS, WHITE, BLACK
)
from entities import Player, Ball
from input_handler import InputHandler

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pong")
screen.fill(BLACK)

player_1 = Player(
    10,
    SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    WHITE)
player_2 = Player(
    SCREEN_WIDTH - PLAYER_WIDTH - 10,
    SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    WHITE)
ball = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, BALL_RADIUS, WHITE)
player1_handler = InputHandler(player_1, pygame.K_w, pygame.K_s)
player2_handler = InputHandler(player_2, pygame.K_o, pygame.K_l)

running = True

while running:
    delta_time = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BLACK)
        player1_handler.handle_input(delta_time, PLAYER_SPEED)
        player2_handler.handle_input(delta_time, PLAYER_SPEED)
        player_1.draw(screen)
        player_2.draw(screen)
        pygame.display.flip()

pygame.quit()
sys.exit()