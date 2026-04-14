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
    def __init__(self, direction:tuple[float, float]):
        self.direction = direction
        print(self.direction)

    def execute(self, entity, delta_time:float, speed:float):
        new_pos = [
            clamp(
                entity.x + self.direction[0] * delta_time * speed,
                5,
                SCREEN_WIDTH - PLAYER_WIDTH - 5
            ),
            clamp(
                entity.y + self.direction[1] * delta_time * speed,
                5,
                SCREEN_HEIGHT - PLAYER_HEIGHT - 5
            )
        ]
        entity.set_x(new_pos[0])
        entity.set_y(new_pos[1])
