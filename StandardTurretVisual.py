from AbstractTurretVisual import AbstractTurretVisual
from pygame import Color,draw,Rect,Surface,SRCALPHA,transform
from math import pi

class StandardTurretVisual(AbstractTurretVisual):
    def __init__(self,size:int,sourceTurret):
        super().__init__(size,size,sourceTurret)
        self.recolorBase(1)
        self.cannonWidth=size*0.6
        self.cannonhigh =size*0.45
        self.canon = Surface((self.cannonWidth,self.cannonhigh ),SRCALPHA)
        self.drawCanon()

    def drawCanon(self):
        self.canon.fill(Color(0,0,0,0))
        width = self.cannonWidth
        high  = self.cannonhigh
        draw.rect(self.canon, Color(255, 0, 0), Rect(0.8 * width, 0.25 * high, 0.2 * width, 0.2 * high))
        draw.rect(self.canon, Color(255, 0, 0), Rect(0.8 * width, 0.55 * high, 0.2 * width, 0.2 * high))
        draw.polygon(self.canon, Color(255, 0, 0),
                     [(0.1 * width, 0), (0.7 * width, 0), (0.8 * width, 0.25 * high), (0.8 * width, 0.75 * high),
                      (0.7 * width, high), (0.1 * width, high)])
        draw.rect(self.canon, Color(0, 0, 0), Rect(0.8 * width, 0.25 * high, 0.2 * width, 0.2 * high),3)
        draw.rect(self.canon, Color(0, 0, 0), Rect(0.8 * width, 0.55 * high, 0.2 * width, 0.2 * high),3)
        draw.polygon(self.canon, Color(0, 0, 0),
                     [(0.1 * width, 0), (0.7 * width, 0), (0.8 * width, 0.25 * high), (0.8 * width, 0.75 * high),
                      (0.7 * width, high), (0.1 * width, high)],5)

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




