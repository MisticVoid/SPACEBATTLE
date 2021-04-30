from LaserTurret import LaserTurret
import time
from math import pi
from pygame import Color,init,display,draw,mouse
import pygame

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
        return (1000,100),(1000,200),(1200,200),(1200,100)

class MockPlayer:
    def hit(self,*args):
        print(args)

    def __init__(self):
        pass
    posX=450
    posY=450
    mousePos=(0,0)

    def getPoints(self):
        mosePos = mouse.get_pos()
        return (mosePos[0],mosePos[1]),(mosePos[0]+100,mosePos[1]),(mosePos[0],mosePos[1]+100)

class MockLevel:
    turrets=[MockObstacle()]
    obstacles=[]
    player=MockPlayer()

def main():
    Tx=50
    Ty=400
    Turret = LaserTurret(Tx,Ty,75,75,10,3,pi/2,pi,3,MockLevel,20)
    init()
    screen = display.set_mode((sizeX, sizeY))
    times = [0] * 10
    i = 0
    t = time.perf_counter_ns()
    while True:
        for event in pygame.event.get():
            pass
        mosePos = mouse.get_pos()
        MockPlayer.posX=mosePos[0]+50
        MockPlayer.posY = mosePos[1]+50
        screen.fill(Color(0,0,0))
        Turret.nextCycle(times[i]/10**9,MockLevel.player.posX,MockLevel.player.posY)
        draw.circle(screen,Color(255,255,255),(MockLevel.player.posX,MockLevel.player.posY),10)
        #draw.circle(screen, Color(255, 0, 0), (Tx, Ty), 10)
        #draw.circle(screen, Color(0, 255, 0), Turret.getPoint(), 3)
        s=Turret.draw()
        screen.blit(s, (Turret.posX, Turret.posY))
        Turret.shoot(MockLevel.player.posX,MockLevel.player.posY)
        draw.polygon(screen,Color(0,255,0),MockPlayer.getPoints(1))
        draw.polygon(screen, Color(0, 0, 255), [(1000,100),(1000,200),(1200,200),(1200,100)])
        Turret.effect(screen)
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