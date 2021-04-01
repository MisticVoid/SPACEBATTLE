from MisselAbstract import *
from StandardMisselVisual import *

class StandardMissile(AbstractMissile):
    def __init__(self, posX: int, posY: int, size: int, damage: int, angle: float, speed: float,colorC: Color):
        super().__init__(posX, posY, size, size, damage, angle, speed)
        self.visual = StandardMissileVisual(size,colorC)

    def nextCycle(self,deltaTime: float) -> None:
        self.move(deltaTime)

    def collision(self):
        pass  # to implement

















