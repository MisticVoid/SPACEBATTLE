import abc
from pygame import Surface,SRCALPHA


class AbstractTurretVisual(abc.ABC):
    def __init__(self,sizeX:int,sizeY:int,sourceTurret,alpha: bool = False):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.sourceTurret=sourceTurret
        if alpha:
            self.surface = Surface((sizeX, sizeY))
        else:
            self.surface = Surface((sizeX, sizeY), SRCALPHA)

    def draw(self):
        pass

    def recolorBase(self,value:float):
        pass
