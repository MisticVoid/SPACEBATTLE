from pygame import Surface
import abc

class AbstractMissileVisual(abc.ABC):
    def __init__(self,sizeX: int,sizeY: int):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.surface = None

    def draw(self) -> Surface:
        pass



