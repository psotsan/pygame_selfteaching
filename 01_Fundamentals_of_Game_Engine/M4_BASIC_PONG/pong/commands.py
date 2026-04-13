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

    def execute(self, entity, delta_time:float, speed:float):
        new_pos = [
            clamp(
                entity.rect.x + self.direction[0] * delta_time * speed,
                5,
                SCREEN_WIDTH - PLAYER_WIDTH - 5
            ),
            clamp(
                entity.rect.y + self.direction[1] * delta_time * speed,
                5,
                SCREEN_HEIGHT - PLAYER_HEIGHT - 5
            )
        ]
        entity.rect.x = new_pos[0]
        entity.rect.y = new_pos[1]
