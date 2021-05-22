from Level import *
import time
import pygame


class GameEngine:
    def __init__(self, playerProperties, menu, level,sound, sizeX = 1920, sizeY=1020, settings = None):
        #pygame.init()
        pygame.display.set_caption("Space Battle")
        loading = MapElement(0, 0, sizeX, sizeY, "loading.jpg")
        surf = loading.draw()
        menu.getScreen().blit(surf, (0,0))
        pygame.display.flip()

        #time.sleep(1)
        self.sounds=sound
        self.runG = False
        self.menu = menu
        self.score = None
        self.level = Level(playerProperties, sizeX, sizeY, self, menu.screen, level, settings=settings,sounds=self.sounds)

    def stop(self):
        self.runG = False
        self.menu.pause()

    def win(self):
        self.score = "Win"
        self.runG = False

    def lose(self):
        self.score = "Lose"
        self.runG = False

    def keepRunning(self):
        self.runG = True



    def run(self):
        self.level.screen.blit(self.level.background, (0, 0))
        times = [0] * 10
        i = 0
        t = time.perf_counter_ns()
        self.runG = True
        while self.runG:

            times[i] = min(time.perf_counter_ns() - t,10**8)
            t = time.perf_counter_ns()
            self.level.update(times[i]/10**9)
            self.level.display()
            i += 1
            i %= 10
            #print("fps:", sum(times))
        return self.score



def sum(T):
    value = 0
    for x in T:
        value+=x
    return 1/((value/10)/10**9)









