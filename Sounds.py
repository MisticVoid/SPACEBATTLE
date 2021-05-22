import os


import pygame



class Sounds:
    def __init__(self, volume):
        self.sounds = {}
        self.sounds["playerShot"] = pygame.mixer.Sound(os.path.join("recourses", "playerShot.wav"))
        self.sounds["playerDamage"] = pygame.mixer.Sound(os.path.join("recourses", "playerDamage.wav"))
        self.sounds["turretDestroyed"] = pygame.mixer.Sound(os.path.join("recourses", "turretDestroyed.wav"))
        self.sounds["rocketShot"] = pygame.mixer.Sound(os.path.join("recourses", "rocketShot.wav"))
        self.sounds["rocketCollision"] = pygame.mixer.Sound(os.path.join("recourses", "rocketCollision.wav"))
        self.sounds["laser"] = pygame.mixer.Sound(os.path.join("recourses", "laser.wav"))
        self.sounds["turretHit"] = pygame.mixer.Sound(os.path.join("recourses", "turretHit.wav"))
        self.sounds["standardShot"] = pygame.mixer.Sound(os.path.join("recourses", "standardShot.wav"))

        for s in self.sounds.values():
            s.set_volume(volume)

    def play(self, soundName):
        self.sounds[soundName].play()