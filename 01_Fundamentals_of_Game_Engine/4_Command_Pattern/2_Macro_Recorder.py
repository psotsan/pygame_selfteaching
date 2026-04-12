from abc import ABC, abstractmethod
import pygame
import sys


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

PLAYER_SIZE = 60
STEPS = PLAYER_SIZE
#MAX_UNDOS = 10

def clamp (val, min_val, max_val):
    return max(min(val, max_val), min_val)


class Player:
    color = pygame.Color(WHITE)
    def __init__(self):
        self.rect = pygame.Rect(
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            PLAYER_SIZE,
            PLAYER_SIZE
        )

    def draw(self, scr:pygame.display):
        pygame.draw.rect(scr, WHITE, self.rect)


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class MoveX(Command):
    def __init__(self, entity:Player, direction):
        self.entity = entity
        self.direction = direction
        self.previous_pos = self.entity.rect.x, self.entity.rect.y

    def execute(self):
        
        new_pos_x = clamp(self.entity.rect.x + self.direction * STEPS,
                          0,
                          SCREEN_WIDTH - PLAYER_SIZE
                          )
        self.entity.rect.x = new_pos_x

    def undo(self):
        self.entity.rect.x = self.previous_pos[0]
        
        
class MoveY(Command):
    def __init__(self, entity:Player, direction):
        self.entity = entity
        self.direction = direction
        self.previous_pos = self.entity.rect.x, self.entity.rect.y

    def execute(self):
        new_pos_y = clamp(self.entity.rect.y + self.direction * STEPS,
                          0,
                          SCREEN_HEIGHT - PLAYER_SIZE
                          )
        self.entity.rect.y = new_pos_y

    def undo(self):
        self.entity.rect.y = self.previous_pos[1]


class InputHandler:
    def __init__(self, entity:Player):
        self.entity = entity
        self.command_stack = []
        self.cmd_i = 0
        self.recording = False
        self.replay = False

    def _toggle_recording(self):
        self.recording = not self.recording
        if self.recording:
            self.command_stack = []
            self.cmd_i = 0

    def _process_command(self, axis, direction):
        match axis:
            case "X":
                cmd = MoveX(self.entity, direction)
            case "Y":
                cmd = MoveY(self.entity, direction)
        cmd.execute()
        if self.recording:
            self.command_stack.append(cmd)
    def update(self):
        if len(self.command_stack) > 0 and self.replay:
            if self.cmd_i >= len(self.command_stack):
                self.replay = False
                self.cmd_i = 0
            else:
                self.command_stack[self.cmd_i].execute()
                self.cmd_i += 1

    def handle_input(self, e:pygame.event):
        if not self.replay and e.type == pygame.KEYDOWN:
            match e.key:
                case pygame.K_w:
                    self._process_command("Y", -1)
                case pygame.K_d:
                    self._process_command("X", 1)
                case pygame.K_s:
                    self._process_command("Y", 1)
                case pygame.K_a:
                    self._process_command("X", -1)
                case pygame.K_g:
                    self._toggle_recording()
                case pygame.K_r:
                    self.recording = False
                    self.replay = True
                    self.cmd_i = 0
                    if len(self.command_stack) > 0:
                        self.entity.rect.x = self.command_stack[0].previous_pos[0]
                        self.entity.rect.y = self.command_stack[0].previous_pos[1]


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Macro Recorder")

screen.fill(BLACK)
player = Player()
player_handler = InputHandler(player)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        player_handler.handle_input(event)

    screen.fill(BLACK)
    player_handler.update()
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()