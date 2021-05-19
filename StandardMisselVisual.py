from AbstractMisselVisual import AbstractMissileVisual
from pygame import Color,SRCALPHA,Surface,draw

class StandardMissileVisual(AbstractMissileVisual):
    def __init__(self, size: int, colorC: Color):
        size*=1.5
        super().__init__(size, size)
        self.surface = Surface((size,size),SRCALPHA)
        self.surface.fill((0,0,0,0))
        draw.circle(self.surface,colorC,(size/2,size/2),size/2)

    def draw(self) -> Surface:
        return self.surface








