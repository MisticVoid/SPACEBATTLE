from RocketTurret import RocketTurret
import time
from math import pi
from pygame import init,display,Color,draw

sizeX = 1920
sizeY = 1080

class MockTarget:
    def __init__(self,a,b):
        self.posX=a
        self.posY=b

def main():
    turret = RocketTurret(225,225,100,100,100,5,pi/5,0,1000,MockTarget(800,800))
    init()
    screen = display.set_mode((sizeX, sizeY))
    a = 0
    times = [0] * 10
    i = 0
    t = time.perf_counter_ns()
    l = 0
    b=0
    missels=[]
    while True:
        screen.fill(Color(0,0,0))
        turret.nextCycle(times[i]/10**9,800,800)
        #print(turret.angle)
        missel=turret.shoot(800,800)
        s=turret.draw()
        screen.blit(s, (turret.posX, turret.posY ))
        if missel is not None:
            missels.append(missel)
        for missel in missels:
            missel.nextCycle(times[i]/10**9)
            s=missel.draw()
            screen.blit(s, (missel.posX - s.get_rect().width / 2, missel.posY - s.get_rect().height / 2))
        draw.circle(screen, Color(255, 255, 255), (800, 800), 10)
        display.flip()
        times[i] = time.perf_counter_ns() - t
        l += times[i]
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