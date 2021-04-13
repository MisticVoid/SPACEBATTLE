from standardMissel import *
from MisselPlacer import *
import time
from math import pi

sizeX = 500
sizeY =500

def main():
    m = MisselPlacer(StandardMissile,{"size": 3,"damage": 100,"speed": 1000,"colorC": Color(255,255,0)})
    p=m.placeMissile((10,10),(100,100),10,pi*9/5)
    init()
    screen = display.set_mode((sizeX, sizeY))
    times = [0] * 10
    i = 0
    t = time.perf_counter_ns()
    l = 0
    while True:
        screen.fill(Color(0,0,0))
        p.nextCycle(times[i]/10**9)
        s = p.draw()

        screen.blit(s, (p.posX - s.get_rect().width / 2, p.posY - s.get_rect().height / 2))

        display.flip()
        times[i] = time.perf_counter_ns() - t
        l += times[i]
        t = time.perf_counter_ns()
        i += 1
        i %= 10
        print("fps:", sum(times))


def sum(T):
    value = 0
    for x in T:
        value += x
    return 1 / ((value / 10) / 10 ** 9)


if __name__ == "__main__":
    main()