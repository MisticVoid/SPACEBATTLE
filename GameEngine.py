from Level import *
import time
import pygame


class GameEngine:
    def __init__(self, playerProperties, sizeX = 1920, sizeY=1020):
        pygame.init()
        pygame.display.set_caption("Space Battle")
        self.runG = False

        self.level = Level(playerProperties, sizeX, sizeY, self)

    def stop(self):
        self.runG = False

    def run(self):
        self.level.screen.blit(self.level.background, (0, 0))
        times = [0] * 10
        i = 0
        t = time.perf_counter_ns()
        self.runG = True
        while self.runG:

            times[i] = min(time.perf_counter_ns() - t,10**8)  # add max value
            t = time.perf_counter_ns()
            self.level.update(times[i]/10**9)
            self.level.display()
            i += 1
            i %= 10
            print("fps:", sum(times))
        else:
            pygame.quit()



def sum(T):
    value = 0
    for x in T:
        value+=x
    return 1/((value/10)/10**9)









