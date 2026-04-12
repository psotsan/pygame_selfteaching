from constants import (
    WHITE, PLAYER_WIDTH, PLAYER_HEIGHT, BALL_RADIUS
)
import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    def draw(self, scr:pygame.display):
        pygame.draw.rect(scr, WHITE, self.rect)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, scr:pygame.display):
        pygame.draw.circle(
            scr,
            WHITE,
            (self.x,self.y),
            BALL_RADIUS
        )