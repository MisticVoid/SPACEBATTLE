from MisselAbstract import *
from StandardMisselVisual import *

class StandardMissile(AbstractMissile):
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, damage: int, angle: float, speed: float):
        super().__init__(posX, posY, sizeX, sizeY, damage, angle, speed)
        self.visual = StandardMissileVisual(5,Color(0,255,0))

    def nextCycle(self,deltaTime: float) -> None:
        self.move(deltaTime)

    def collision(self):
        pass  # to implement

















