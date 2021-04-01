from Level import *
import time
import pygame


class GameEngine:
    def __init__(self, playerProperties, sizeX = 1920, sizeY=1020):
        pygame.init()
        pygame.display.set_caption("Space Battle")

        self.level = Level(playerProperties, sizeX, sizeY, self)

    def stop(self):
        self.run = False

    def run(self):
        self.level.screen.blit(self.level.background, (0, 0))
        a = 0
        times = [0] * 10
        i = 0
        t = time.perf_counter_ns()
        self.run = True
        while self.run:

            times[i] = time.perf_counter_ns() - t

            self.level.update(times[i])
            self.level.display()

            t = time.perf_counter_ns()
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









