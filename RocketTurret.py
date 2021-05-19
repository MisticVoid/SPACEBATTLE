from TurretAbstract import AbstractTurret
from RocketMissile import RocketMissile
from RocketTurretVisual import RocketTurretVisual
from math import pi
from pygame import Color
from MisselPlacer import MisselPlacer

from MisselAbstract import AbstractMissile
from Geometry import twoPointToLine,distPointFromLine,rotatePoint,orient,squarePointDis

class RocketTurret(AbstractTurret):
    def __init__(self, posX: int, posY: int, size:int,damage:int, maxHealth: int, coolDown: float,
                 rotationSpeed: float, angle: float, bulletSpeed: int,player):
        super().__init__(posX, posY, size, size, maxHealth, coolDown, rotationSpeed, angle)
        self.disLim = 50
        self.visual = RocketTurretVisual(size, self)
        self.missilePlacer = MisselPlacer(RocketMissile, {"sizeX":20,"sizeY":10,"damage":damage,"speed":bulletSpeed,"rotationSpeed":pi/2,
                          "colorC":Color(255,0,0),"target":player})

    def shotSound(self):
        return "rocketShot"

    def effect(self,screen,screenX,screenY,x,y):
        pass












