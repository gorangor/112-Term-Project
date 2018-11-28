import pygame
from setup import *
from Maze import *
from pygamegame import *
class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.mS = 32
        self.iS = round(1/self.mS*700) + 1
        self.speedX = 0
        self.speedY = 0
        self.image = pygame.transform.scale(pygame.image.load(image),((round(1/self.mS * 700) - 1, round(1/self.mS * 700) - 1)))
        self.rect = self.image.get_rect()
        self.rect.x = round(1/self.mS * 700) + 1
        self.rect.y = round(1/self.mS * 700) + 1
        self.oldX = 0
        self.oldY = 0
        self.speed = 5
        self.health = 100
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
class Player2(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.mS = 32
        self.iS = round(1 / self.mS * 700) + 1
        self.speedX = 0
        self.speedY = 0
        self.image = pygame.transform.scale(pygame.image.load(image),
                                            ((round(1 / self.mS * 700) - 1, round(1 / self.mS * 700) - 1)))
        self.rect = self.image.get_rect()
        self.rect.x = round(1 / self.mS * 700) + 1
        self.rect.y = round(1 / self.mS * 700) + 1
        self.oldX = 0
        self.oldY = 0
        self.speed = 5
        self.health = 100
        self.mode = "Can Copy"
        self.copies = []
    def clone(self):
        self.copies.append((self.rect.x, self.rect.y))
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
        for clones in self.copies:
            screen.blit(self.image, (clones[0], clones[1]))


class Maze(pygame.sprite.Sprite):
    def __init__(self):
        self.mS = 32
        self.iS = round(1/self.mS*700) + 1
        self.lst = maze(lstMaker(self.mS-1), self.mS)
        self.image = pygame.transform.scale(pygame.image.load("wall_mid.png"), (self.iS, self.iS))
        self.locations = []
    def draw(self):
        for rows in range(len(self.lst)):
            for cols in range(0, len(self.lst)):
                if not self.lst[rows][cols]:
                    screen.blit(self.image, (rows/self.mS * 700, cols/self.mS * 700))
                    if (rows/self.mS * 700, cols/self.mS * 700) not in self.locations:
                        self.locations.append((rows/self.mS * 700, cols/self.mS * 700))
class Sword(pygame.sprite.Sprite):
    def __init__(self,x,y,iS):
        self.damage = 100
        self.charge = 0
        self.image = pygame.transform.scale(pygame.image.load("Sword_Right.png"), (iS//2, iS//2))
        self.rect = self.image.get_rect()
        self.rect.x = x + iS/2
        self.rect.y = y + iS/2
        self.mode = "Not Thrown"
        self.direction = "Right"
        self.speedX = 0
        self.speedY = 0
    def throw(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
