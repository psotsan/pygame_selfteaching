# Command pattern implemented, with undo logic

from abc import ABC, abstractmethod
import pygame
import sys

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

PLAYER_SIZE = 30

def clamp(val, min_val, max_val):
    return max(min(val, max_val), min_val)


class Player:
    color = pygame.Color(WHITE)
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 30, 30)

    def draw(self, scr:pygame.display):
        pygame.draw.rect(scr, WHITE, self.rect)


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class MoveCommand(Command):
    def __init__(self, entity: Player, direction, velocity):
        self.entity = entity
        self.dir = direction
        self.velocity = velocity
        self.previous_pos = [self.entity.rect.x, self.entity.rect.y]

    def execute(self):
        self.previous_pos = (self.entity.rect.x, self.entity.rect.y)
        new_pos = [
            clamp(self.entity.rect.x + self.dir[0] * self.velocity[0], 0, SCREEN_WIDTH - PLAYER_SIZE),
            clamp(self.entity.rect.y + self.dir[1] * self.velocity[1], 0, SCREEN_HEIGHT - PLAYER_SIZE)
        ]

        self.entity.rect.x = new_pos[0]
        self.entity.rect.y = new_pos[1]

    def undo(self):
        self.entity.rect.x, self.entity.rect.y = self.previous_pos


class InputHandler:
    velocity = (10, 10)

    def __init__(self, entity: Player):
        self.entity = entity
        self.command_stack = []

    def handle_input(self):
        keys = pygame.key.get_pressed()
        direction = [0, 0]
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            direction[0] = -1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction[1] = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction[0] = 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction[1] = 1
        if keys[pygame.K_z]:
            if len(self.command_stack) > 0:
                cmd = self.command_stack.pop()
                cmd.undo()
        #self.move_command.execute(direction, self.velocity)
        if direction != [0, 0]:
            cmd = MoveCommand(self.entity, direction, self.velocity)
            cmd.execute()
            # undo until 5 seconds
            if len(self.command_stack) > 300:
                self.command_stack.pop(0)
            self.command_stack.append(cmd)


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Undoable Commands")

screen.fill(BLACK)
player = Player()
player_handler = InputHandler(player)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BLACK)
    player_handler.handle_input()
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()