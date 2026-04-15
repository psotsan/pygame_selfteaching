from entities import Player
from commands import MoveCommand
from constants import SCREEN_HEIGHT
import pygame


class InputHandler:
    def __init__(self, entiy:Player,
                 control_up:pygame.key,
                 control_down:pygame.key):
        self.entity = entiy
        self.control_up = control_up
        self.control_down = control_down
        self.command_up = MoveCommand((0., -1.))
        self.command_down = MoveCommand((0., 1.))

    def handle_input(self, delta_time:float, speed:float):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[self.control_up]:
            self.command_up.execute(self.entity, delta_time, speed)
        if pressed_keys[self.control_down]:
            self.command_down.execute(self.entity, delta_time, speed)