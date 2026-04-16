from abc import ABC, abstractmethod
from utils import clamp
from constants import (
    SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT
)

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class MoveCommand(Command):
    def __init__(self, direction:list):
        self.direction = direction

    def execute(self, entity, delta_time:float, speed:float, bottom_limit=SCREEN_HEIGHT - PLAYER_HEIGHT - 5):
        new_pos = [
            clamp(
                entity.x + self.direction[0] * delta_time * speed,
                5,
                SCREEN_WIDTH - PLAYER_WIDTH - 5
            ),
            clamp(
                entity.y + self.direction[1] * delta_time * speed,
                5,
                bottom_limit
            )
        ]
        entity.set_x(new_pos[0])
        entity.set_y(new_pos[1])
