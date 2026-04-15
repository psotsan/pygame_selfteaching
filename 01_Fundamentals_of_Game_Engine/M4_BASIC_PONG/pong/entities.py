import pygame, random

class Player:
    def __init__(self, x:int, y:int, width:int, height:int, color:pygame.Color):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = self.rect.x
        self.y = self.rect.y
        self.color = color

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
        self.direction = random.randrange(0, 360)


    def draw(self, scr:pygame.display):
        pygame.draw.circle(
            scr,
            self.color,
            (self.x,self.y),
            self.radius
        )

    def collide(self):
        pass

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y