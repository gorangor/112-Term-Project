import pygame
from setup import *
from Maze import *
from pygamegame import *
mS = 30git
iS = round(1/mS*700) + 1
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedX = 0
        self.speedY = 0
        self.image = pygame.transform.scale(pygame.image.load("Ice Zombie.png"),((round(1/mS * 700) - 1, round(1/mS * 700) - 1)))
        self.rect = self.image.get_rect()
        self.rect.x = round(1/mS * 700) + 1
        self.rect.y = round(1/mS * 700) + 1
        self.oldX = 0
        self.oldY = 0
    def gottaGoFastX(self, dx):
        self.speedX = dx
    def gottaGoFastY(self, dy):
        self.speedY = dy
    def update(self):
        self.oldX = self.rect.x
        self.oldY = self.rect.y
        self.rect.x += self.speedX
        self.rect.y += self.speedY
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Maze(pygame.sprite.Sprite):
    def __init__(self):
        self.lst = maze(lstMaker(mS-1), mS)
        self.image = pygame.transform.scale(pygame.image.load("wall_mid.png"), (iS, iS))
        self.locations = []
    def draw(self):
        for rows in range(len(self.lst)):
            for cols in range(len(self.lst[rows])):
                if not self.lst[rows][cols]:
                    screen.blit(self.image, (rows/mS * 700, cols/mS * 700))
                    if (rows/mS * 700, cols/mS * 700) not in self.locations:
                        self.locations.append((rows/mS * 700, cols/mS * 700))
