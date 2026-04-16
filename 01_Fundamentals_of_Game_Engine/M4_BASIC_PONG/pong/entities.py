import pygame, random
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, INITIAL_BALL_SPEED, PLAYER_SPEED,
    PLAYER_HEIGHT, PLAYER_WIDTH)

class Player:
    def __init__(self, x:int, y:int, width:int, height:int, color:pygame.Color):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = self.rect.x
        self.y = self.rect.y
        self.color = color
        self.speed = PLAYER_SPEED

    def draw(self, scr:pygame.display):
        pygame.draw.rect(scr, self.color, self.rect)

    def set_x(self, x:int):
        self.x = x
        self.rect.x = x

    def set_y(self, y:int):
        self.y = y
        self.rect.y = y


class Ball:
    def __init__(self, x:int, y:int, radius:int, color:pygame.Color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = INITIAL_BALL_SPEED
        #self.direction = random.randrange(0, 360)


    def draw(self, scr:pygame.display):
        pygame.draw.circle(
            scr,
            self.color,
            (self.x,self.y),
            self.radius
        )

    def collide(self, p1_pos, p2_pos) -> str:
        if self.y >= (SCREEN_HEIGHT - self.radius) or self.y <= self.radius:
            return "y"
        if (self.x <= p1_pos[0] + PLAYER_WIDTH + self.radius
            and self.y >= p1_pos[1]
            and self.y <= p1_pos[1] + PLAYER_HEIGHT):
            return "left_paddle"
        if (self.x >= p2_pos[0] - self.radius
            and self.y >= p2_pos[1]
            and self.y <= p2_pos[1] + PLAYER_HEIGHT):
            return "right_paddle"
        if self.x <= self.radius:
            return "x_left"
        if self.x >= SCREEN_WIDTH - 2 * self.radius:
            return "x_right"

        return "none"

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y