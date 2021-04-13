from standardMissel import *
from Player import Player
import time
from math import pi

sizeX = 500
sizeY = 500

def main():
    player = Player(250, 250, 0, 500, 250, 100, 0, pi/2, 75, 50, 10, 10, 0.7,1000)
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
        player.rotateLeft(times[i]/10**9)
        player.nextCycle(times[i]/10**9)
        missel=player.shoot()
        s = player.draw()


        screen.blit(s, (player.posX - s.get_rect().width / 2, player.posY - s.get_rect().height / 2))
        if missel is not None:
            missels.append(missel)
        for missel in missels:
            missel.nextCycle(times[i]/10**9)
            s=missel.draw()
            screen.blit(s, (missel.posX - s.get_rect().width / 2, missel.posY - s.get_rect().height / 2))

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