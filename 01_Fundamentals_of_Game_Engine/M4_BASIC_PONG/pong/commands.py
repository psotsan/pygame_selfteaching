from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class MoveUp(Command):
    def __init__(self, entity):
        self.entity = entity

    def execute(self):
        pass


class MoveDown(Command):
    def __init__(self, entity):
        self.entity = entity

    def execute(self):
        pass


class MoveLeft(Command):
    def __init__(self, entity):
        self.entity = entity

    def execute(self):
        pass


class MoveRight(Command):
    def __init__(self, entity):
        self.entity = entity

    def execute(self):
        pass