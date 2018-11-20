import pygame
from Classes import *
from pygamegame import *


class Game(PygameGame):
    def init(self):
        Orc.init()
        self.orcGroup = pygame.sprite.Group(Orc(self.width, self.height))

    def timerFired(self, dt):
        self.orcGroup.update(self.isKeyPressed, self.width, self.height)

    def redrawAll(self, screen):
        self.zombieGroup.draw(screen)

Game(600, 600).run()