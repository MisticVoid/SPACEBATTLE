from AbstractMisselVisual import *

class StandardMissileVisual(AbstractMissileVisual):
    def __init__(self, size: int, colorC: Color):
        super().__init__(size, size)
        self.surface = Surface((size,size),SRCALPHA)
        self.surface.fill((0,0,0,0))
        draw.circle(self.surface,colorC,(size/2,size/2),size)

    def draw(self) -> Surface:
        return self.surface








