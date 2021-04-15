from RocketMissile import RocketMissile
import time
from math import pi
from pygame import Color,init,display,draw

sizeX = 1920
sizeY =1080

class MockTarget:
    def __init__(self,a,b):
        self.posX=a
        self.posY=b

def main():
    missile = RocketMissile(200,500,20,10,10,pi/2,500,pi,Color(255,0,0),MockTarget(800,800))
    init()
    screen = display.set_mode((sizeX, sizeY))
    a = 0
    times = [0] * 10
    i = 0
    t = time.perf_counter_ns()
    l = 0
    while True:
        screen.fill(Color(0,0,0))
        missile.nextCycle(times[i]/10**9)
        s = missile.draw()
        draw.circle(screen,Color(255,255,255),(800,800),10)
        screen.blit(s, (missile.posX - s.get_rect().width / 2, missile.posY - s.get_rect().height / 2))

        display.flip()
        times[i] = time.perf_counter_ns() - t
        l += times[i]
        a = l // 10 ** 7
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