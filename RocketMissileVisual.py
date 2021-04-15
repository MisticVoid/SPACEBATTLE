from AbstractMisselVisual import AbstractMissileVisual
from pygame import Color,SRCALPHA,Surface,draw,Rect,transform
from math import pi

class RocketMissileVisual(AbstractMissileVisual):
    def __init__(self, sizeX: int,sizeY: int, colorC: Color,sourceRocket):
        super().__init__(sizeX, sizeY)
        self.surface = Surface((sizeX,sizeY),SRCALPHA)
        self.surface.fill((0,0,0,0))
        self.sourceRocket=sourceRocket
        self.drawRocket(colorC)

    def drawRocket(self,colorC: Color):
        draw.polygon(self.surface,Color(150,150,150,255),[(0,0),(self.sizeX/3,self.sizeY/2),(0,self.sizeY)])
        draw.rect(self.surface,Color(255,255,255,255),Rect(0.15*self.sizeX,0,self.sizeX*0.35,self.sizeY))
        draw.polygon(self.surface,colorC,[(self.sizeX,self.sizeY/2),(self.sizeX*0.5,self.sizeY),(self.sizeX*0.5,0)])

    def draw(self) -> Surface:
        return self.__rotate(self.sourceRocket.angle)

    def __rotate(self,angle: float) -> Surface:
        return transform.rotate(self.surface,angle*180/pi)




