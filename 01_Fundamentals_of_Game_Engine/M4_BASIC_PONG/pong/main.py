import pygame, sys, random
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED, INITIAL_BALL_SPEED,
    PLAYER_WIDTH, PLAYER_HEIGHT, BALL_RADIUS, WHITE, BLACK
)
from entities import Player, Ball
from input_handler import InputHandler
from commands import MoveCommand
from utils import ball_initial_direction, score

pygame.init()

scores = {
    1: 0,
    2: 0,
}

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pong")
screen.fill(BLACK)

player_1 = Player(
    3 * BALL_RADIUS,
    SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    WHITE)
player_2 = Player(
    SCREEN_WIDTH - PLAYER_WIDTH - 3 * BALL_RADIUS,
    SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    WHITE)

ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS, WHITE)

player1_handler = InputHandler(player_1, pygame.K_w, pygame.K_s)
player2_handler = InputHandler(player_2, pygame.K_o, pygame.K_l)

ball_x_dir, ball_y_dir = ball_initial_direction()
ball_move_command = MoveCommand([ball_x_dir, ball_y_dir])
ball_speed = INITIAL_BALL_SPEED

running = True

while running:
    delta_time = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    ball_col = ball.collide((player_1.x, player_1.y), (player_2.x, player_2.y))
    if ball_col == "y":
        ball_move_command.direction[1] = -1 * ball_move_command.direction[1]
        ball_speed += INITIAL_BALL_SPEED * 0.02
    if ball_col == ("left_paddle") or ball_col == ("right_paddle"):
        ball_move_command.direction[0] = -1 * ball_move_command.direction[0]
        ball_speed += INITIAL_BALL_SPEED * 0.02
        ball.set_x(ball.x + BALL_RADIUS if ball_col == "left_paddle" else ball.x - BALL_RADIUS)
    if ball_col == "x_left":
        score(scores, 2)
        ball_x_dir, ball_y_dir = ball_initial_direction()
        ball_speed = INITIAL_BALL_SPEED
        ball.set_x(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2)
        ball.set_y(SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2)
        ball_move_command = MoveCommand([ball_x_dir, ball_y_dir])
    if ball_col == "x_right":
        score(scores, 1)
        ball_x_dir, ball_y_dir = ball_initial_direction()
        ball_speed = INITIAL_BALL_SPEED
        ball.set_x(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2)
        ball.set_y(SCREEN_HEIGHT // 2 - PLAYER_HEIGHT // 2)
        ball_move_command = MoveCommand([ball_x_dir, ball_y_dir])
    print(ball_speed)
    screen.fill(BLACK)
    player1_handler.handle_input(delta_time, PLAYER_SPEED)
    player2_handler.handle_input(delta_time, PLAYER_SPEED)
    ball_move_command.execute(ball, delta_time, ball_speed, SCREEN_HEIGHT)
    player_1.draw(screen)
    player_2.draw(screen)
    ball.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()