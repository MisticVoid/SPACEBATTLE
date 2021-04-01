import pygame
from Player import *
from GameEngine import *

class Level:
    def __init__(self, playerProperties, sizeX: int, sizeY: int, gameEngine):
        self.screenSizeX = sizeX
        self.screenSizeY = sizeY  # Probably redundant because of: screen.get_size()

        self.screen = pygame.display.set_mode((sizeX, sizeY))
        mapX, mapY = sizeX*2, sizeY*2
        self.background = pygame.Surface((mapX, mapY))
        self.engine = gameEngine

        p = playerProperties
        self.player = Player(mapX/4, mapY/4, p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12])

        for i in range (40,0,-1):
            pygame.draw.circle(self.background, (i*2, i*2, i*2), (mapX//2, mapY//2), i*100)

    def update(self, deltaTime):
        self.player.nextCycle(deltaTime / 10 ** 9)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.engine.stop()

        keys = pygame.key.get_pressed()

        print(self.player.posX, self.player.posY)


        if keys[K_UP]:
            self.player.accelerate(deltaTime / 10**6)
        if keys[K_DOWN]:
            self.player.reduceSpeed(deltaTime / 10**6)
        if keys[K_LEFT]:
            self.player.rotateLeft(deltaTime / 10 ** 9)
        if keys[K_RIGHT]:
            self.player.rotateRight(deltaTime / 10 ** 9)





    def display(self):
        s = self.player.draw()
        x, y = int(self.player.posX), int(self.player.posY)
        bg = self.background.copy()
        bg.scroll(-x, -y)
        self.screen.blit(bg, (0, 0))
        pygame.draw.circle(s, (255, 0, 0), (s.get_rect().width // 2, s.get_rect().height // 2), 1)
        self.screen.blit(s, (self.screenSizeX//2 - s.get_rect().width//2, self.screenSizeY//2 - s.get_rect().height//2))

        pygame.display.flip()

