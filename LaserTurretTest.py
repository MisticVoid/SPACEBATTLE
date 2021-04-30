from LaserTurret import LaserTurret
import time
from math import pi
from pygame import Color,init,display,draw

sizeX = 1920
sizeY =1080



class MockTarget:
    def __init__(self,a,b):
        self.posX=a
        self.posY=b

class MockMisselGenerator:
    hitcor=None
    def __init__(self):
        pass

    def damage(self,player):
        print("hit")
        self.hitcor=player

class MockObstacle:
    def getPoints(self):
        return (100,100),(100,200),(200,200),(200,100)

class MockPlayer:
    def __init__(self):
        pass
    posX=450
    posY=450

    def getPoints(self):
        return ((400,400),(500,400),(400,500))

class MockLevel:
    turrets=[MockObstacle()]
    obstacles=[]
    player=MockPlayer()

def main():
    Tx=0
    Ty=0
    Turret = LaserTurret(Tx,Ty,20,20,10,3,pi/2,pi,MockMisselGenerator,3,MockLevel,{})
    init()
    screen = display.set_mode((sizeX, sizeY))
    times = [0] * 10
    i = 0
    t = time.perf_counter_ns()
    while True:
        screen.fill(Color(0,0,0))
        Turret.nextCycle(times[i]/10**9,MockLevel.player.posX,MockLevel.player.posY)
        draw.circle(screen,Color(255,255,255),(MockLevel.player.posX,MockLevel.player.posY),10)
        draw.circle(screen, Color(255, 0, 0), (Tx, Ty), 10)
        draw.circle(screen, Color(0, 255, 0), Turret.getPoint(), 3)
        #screen.blit(s, (missile.posX - s.get_rect().width / 2, missile.posY - s.get_rect().height / 2))
        Turret.shoot(MockLevel.player.posX,MockLevel.player.posY)
        display.flip()
        times[i] = time.perf_counter_ns() - t
        t = time.perf_counter_ns()
        i += 1
        i %= 10
        #print("fps:", sum(times))


def sum(T):
    value = 0
    for x in T:
        value += x
    return 1 / ((value / 10) / 10 ** 9)


if __name__ == "__main__":
    main()