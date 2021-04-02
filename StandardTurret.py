from TurretAbstract import *
from math import sin,cos,sqrt

class StandardTurret(AbstractTurret):
    def __init__(self, posX: int, posY: int, size: int, damage: int, maxHealth: int, coolDown: float,
                 rotationSpeed: float,angle: float,bulletSpeed: int):
        super().__init__(posX, posY, size, size, damage, maxHealth, coolDown, rotationSpeed,angle)
        print(bulletSpeed)
        self.bulletSpeed = bulletSpeed
        #self.visual =

    def getCrossPoint(self,posX: float,posY: float,speed: float,angle: float) -> Tuple[float,float]:  # where to aim
        # Vx1 = speed * cos(angle)
        # Vy1 = speed * sin(-angle)
        # print(Vx1,Vy1)
        # deltaX = (posX-self.posX)
        # deltaY = (posY-self.posY)
        # a=(deltaY*Vx1-deltaX*Vy1)/self.bulletSpeed
        # print(self.bulletSpeed)
        # print("a",a)
        # k = (a-sqrt(2-a**2))/2
        # Vx2 = self.bulletSpeed * sqrt(1-k**2)
        # Vy2 = self.bulletSpeed * k
        # if Vx2 == 0:
        #     x = self.posX
        # else:
        #     x=(posX-Vx1/Vx2*self.posX)/(1-Vx1/Vx2)
        # if Vy2 == 0:
        #     y = self.posY
        # else:
        #     y = (posY - Vy1 / Vy2 * self.posY) / (1 - Vy1 / Vy2)
        # return x,y
        return posX,posY






























