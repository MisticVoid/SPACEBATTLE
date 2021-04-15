import abc
from pygame import Color,draw,Rect,Surface,SRCALPHA,transform
from math import pi


class AbstractTurretVisual(abc.ABC):
    def __init__(self,sizeX:int,sizeY:int,sourceTurret,alpha: bool = False):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.sourceTurret=sourceTurret
        if alpha:
            self.surface = Surface((sizeX, sizeY))
        else:
            self.surface = Surface((sizeX, sizeY), SRCALPHA)
        self.cannonWidth=0
        self.cannonhigh =0
        self.canon = None

    def draw(self):
        surf2=transform.rotate(self.canon,self.sourceTurret.angle*180/pi)
        posBegin=self.sizeX//2-surf2.get_rect().width//2,self.sizeY//2-surf2.get_rect().height//2
        copy=self.surface.copy()
        copy.blit(surf2,posBegin)
        return copy

    def recolorBase(self,value:float):
        edge = Color(int(min(255 * (2 - 2 * value), 255)), int(min(255 * value * 2, 255)), 0)
        self.surface.fill(edge)
        draw.rect(self.surface, Color(0, 0, 0),
                  Rect(self.sizeX / 10, self.sizeY / 10, self.sizeX * 0.8, self.sizeY * 0.8))
        draw.circle(self.surface, Color(0, 0, 80), (self.sizeX / 2, self.sizeX / 2), (self.sizeX * 0.4))

    def drawCanon(self):
        pass
