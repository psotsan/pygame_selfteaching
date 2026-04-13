import pygame

class Player:
    def __init__(self, x:int, y:int, width:int, height:int, color:pygame.Color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, scr:pygame.display):
        pygame.draw.rect(scr, self.color, self.rect)


class Ball:
    def __init__(self, x:int, y:int, radius:int, color:pygame.Color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, scr:pygame.display):
        pygame.draw.circle(
            scr,
            self.color,
            (self.x,self.y),
            self.radius
        )