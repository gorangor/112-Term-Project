import pygame
import random
from Classes import *
from setup import *
#Framework by Lucas Peraza


class PygameGame(object):

    def init(self):
        self.mode = "Start"
        self.image = "Ice Zombie.png"
        self.image2 = "Masked Orc.png"
        self.player = Player(self.image)
        self.player2 = Player2(self.image2)
        self.player2.rect.x = 665 - self.player.rect.x
        self.player2.rect.y = 660 - self.player.rect.y
        self.maze = Maze()
        self.sword = Sword(self.player.rect.x, self.player.rect.y, self.player.iS)
        self.count = 0
        self.cloneTimer = 0
        self.level = 16
        self.time = 60
        self.timeCount = 0
        self.powerUps = []
        self.winner = ""

    def mousePressed(self, x, y):
        print(x,y)
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if self.mode == "Play":
            if keyCode == pygame.K_p:
                self.sword.mode = "Thrown"
            if keyCode == pygame.K_RIGHT:
                self.player.gottaGoFastX(self.player.speed)
                if self.sword.mode == "Not Thrown":
                    self.sword.image = pygame.transform.scale(pygame.image.load("Sword_Right.png"), (self.player.iS//3, self.player.iS//3))
                    self.sword.direction = "Right"
            elif keyCode == pygame.K_LEFT:
                self.player.gottaGoFastX(-self.player.speed)
                if self.sword.mode == "Not Thrown":
                    self.sword.image = pygame.transform.scale(pygame.image.load("Sword_Left.png"), (self.player.iS//3, self.player.iS//3))
                    self.sword.direction = "Left"
            if keyCode == pygame.K_DOWN:
                self.player.gottaGoFastY(self.player.speed)
                if self.sword.mode == "Not Thrown":
                    self.sword.image = pygame.transform.scale(pygame.image.load("Sword_Down.png"), (self.player.iS//3, self.player.iS//3))
                    self.sword.direction = "Down"
            elif keyCode == pygame.K_UP:
                self.player.gottaGoFastY(-self.player.speed)
                if self.sword.mode == "Not Thrown":
                    self.sword.image = pygame.transform.scale(pygame.image.load("Sword_Up.png"), (self.player.iS//3, self.player.iS//3))
                    self.sword.direction = "Up"
            if keyCode == pygame.K_d:
                self.player2.gottaGoFastX(self.player2.speed)
            elif keyCode == pygame.K_a:
                self.player2.gottaGoFastX(-self.player2.speed)
            if keyCode == pygame.K_s:
                self.player2.gottaGoFastY(self.player2.speed)
            elif keyCode == pygame.K_w:
                self.player2.gottaGoFastY(-self.player2.speed)
            if keyCode == pygame.K_SPACE:
                if self.player2.mode == "Can Copy":
                    self.player2.clone()
                    self.player2.mode = "Cant Copy"
        #MODES
        elif self.mode == "Adjust":
            if keyCode == pygame.K_RIGHT and 15 <= self.player.mS <= 63:

                self.player.mS += 4
                self.player2.mS += 4
                self.maze.mS += 4
                self.player.iS = round(1 / self.player.mS * 700) - 1
                self.player.rect.x = round(1 / self.player.mS * 700) - 1
                self.player.rect.y = round(1 / self.player.mS * 700) - 1
                self.player2.iS = round(1 / self.player.mS * 700) - 1
                self.player2.rect.x = 690 - (2 * self.maze.iS)
                self.player2.rect.y = 690 - (2 * self.maze.iS)
                self.maze.iS = round(1 / self.maze.mS * 700) + 1
                self.maze.lst = maze(lstMaker(self.maze.mS - 1), self.maze.mS)
                self.player.image = pygame.transform.scale(pygame.image.load(self.image),
                                                           ((self.player.iS, self.player.iS)))
                self.player2.image = pygame.transform.scale(pygame.image.load(self.image2),
                                                            (self.player2.iS, self.player2.iS))
                self.maze.image = pygame.transform.scale(pygame.image.load("wall_mid.png"),
                                                         (self.maze.iS, self.maze.iS))
                self.sword = Sword(self.player.rect.x, self.player.rect.y, self.player.iS)

            elif keyCode == pygame.K_LEFT and 17 <= self.player.mS <= 65:
                self.player.mS -= 4
                self.player2.mS -= 4
                self.maze.mS -= 4
                self.player.iS = round(1 / self.player.mS * 700) - 1
                self.player.rect.x = round(1 / self.player.mS * 700) - 1
                self.player.rect.y = round(1 / self.player.mS * 700) - 1
                self.player2.iS = round(1 / self.player.mS * 700) - 1
                self.player2.rect.x = 690 - (3 * self.maze.iS)
                self.player2.rect.y = 690 - (3 * self.maze.iS)
                self.maze.iS = round(1 / self.maze.mS * 700) + 1
                self.maze.lst = maze(lstMaker(self.maze.mS - 1), self.maze.mS)
                self.player.image = pygame.transform.scale(pygame.image.load(self.image),
                                                           ((self.player.iS, self.player.iS)))
                self.player2.image = pygame.transform.scale(pygame.image.load(self.image2),
                                                            (self.player2.iS, self.player2.iS))
                self.maze.image = pygame.transform.scale(pygame.image.load("wall_mid.png"),
                                                         (self.maze.iS, self.maze.iS))
                self.sword = Sword(self.player.rect.x, self.player.rect.y, self.player.iS)
            elif keyCode == pygame.K_SPACE:
                self.mode = "Play"
                print(mazeDraw(self.maze.lst))
                print((self.player2.rect.x, self.player2.rect.y))
                print(self.player.iS)
        elif self.mode == "Start":
            if keyCode == pygame.K_SPACE:
                #Easy mode
                self.player.mS = self.level
                self.maze.mS = self.level
                self.player2.mS = self.level
                self.player.iS = round(1 / self.player.mS * 700) -1
                self.player.rect.x = round(1 / self.player.mS * 700) - 1
                self.player.rect.y = round(1 / self.player.mS * 700) - 1
                self.player2.iS = round(1 / self.player.mS * 700) - 1
                self.player2.rect.x = 700 - (6 * self.maze.iS)
                self.player2.rect.y = 700 - (6 * self.maze.iS)
                self.maze.iS = round(1 / self.maze.mS * 700) + 1
                self.maze.lst = maze(lstMaker(self.maze.mS - 1), self.maze.mS)
                self.player.image = pygame.transform.scale(pygame.image.load(self.image),
                                                           ((self.player.iS, self.player.iS)))
                self.player2.image = pygame.transform.scale(pygame.image.load(self.image2),
                                                            (self.player2.iS, self.player2.iS))
                self.maze.image = pygame.transform.scale(pygame.image.load("wall_mid.png"),
                                                         (self.maze.iS, self.maze.iS))
                self.mode = "Play"
                self.sword = Sword(self.player.rect.x, self.player.rect.y, self.player.iS)
            elif keyCode == pygame.K_a:
                self.mode = "Adjust"
            pass

    def keyReleased(self, keyCode, modifier):
        if keyCode == pygame.K_RIGHT:
            self.player.gottaGoFastX(0)
        if keyCode == pygame.K_LEFT:
            self.player.gottaGoFastX(0)
        if keyCode == pygame.K_DOWN:
            self.player.gottaGoFastY(0)
        if keyCode == pygame.K_UP:
            self.player.gottaGoFastY(0)
        if keyCode == pygame.K_d:
            self.player2.gottaGoFastX(0)
        if keyCode == pygame.K_a:
            self.player2.gottaGoFastX(0)
        if keyCode == pygame.K_s:
            self.player2.gottaGoFastY(0)
        if keyCode == pygame.K_w:
            self.player2.gottaGoFastY(0)

    def timerFired(self, dt):
        #Timer
        if self.mode == "Play":
            self.timeCount += 1
            for locations in self.maze.locations:
                x = random.choice(range(0, 700 - self.maze.iS))
                y = random.choice(range(0, 700 - self.maze.iS))
                if locations[0] <= x <= locations[0] + self.maze.iS*3 and locations[1] <= y <= locations[
                    1] + self.maze.iS*3:
                    self.powerUps.append((x, y))
                    break
            if self.timeCount == 10:
                self.time -= 1
                self.timeCount = 0

                print(self.powerUps)
        #COLLISIONS YAY
        for locations in self.maze.locations:
            if locations[0] - self.maze.iS/1.5 <= self.player.rect.x <= locations[0] + self.maze.iS/1.5 and \
                    locations[1] - self.maze.iS/1.5 <= self.player.rect.y <= locations[1] + self.maze.iS/1.5:
                self.player.rect.x = self.player.oldX
                self.player.rect.y = self.player.oldY
            if locations[0] - self.maze.iS/1.5 <= self.player2.rect.x <= locations[0] + self.maze.iS/1.5 and\
                    locations[1] - self.maze.iS/1.5 <= self.player2.rect.y <= locations[1] + self.maze.iS/1.5:
                self.player2.rect.x = self.player2.oldX
                self.player2.rect.y = self.player2.oldY
            if locations[0] <= self.sword.rect.x <= locations[0] + self.maze.iS and \
                    locations[1] <= self.sword.rect.y <= locations[1] + self.maze.iS and self.sword.mode == "Thrown":
                self.count += 50
                self.sword.speedX = 0
                self.sword.speedY = 0
                self.sword.rect.x = self.player.rect.x + self.player.iS/2
                self.sword.rect.y = self.player.rect.y + self.player.iS/2
        if self.player2.rect.x - 10 <= self.player.rect.x <= self.player2.rect.x + 10 and\
                self.player2.rect.y - 10 <= self.player.rect.y <= self.player2.rect.y + 10:
            self.player2.rect.x = self.player2.oldX
            self.player2.rect.y = self.player2.oldY
        if self.player.rect.x - 10 <= self.player2.rect.x <= self.player.rect.x + 10 and\
                self.player.rect.y - 10 <= self.player2.rect.y <= self.player.rect.y + 10:
            self.player.rect.x = self.player.oldX
            self.player.rect.y = self.player.oldY
        if self.sword.rect.x - 20 <= self.player2.rect.x <= self.sword.rect.x + 20 and \
                self.sword.rect.y - 20 <= self.player2.rect.y <= self.sword.rect.y + 20:
            self.count += 25
            self.player2.health -= self.sword.damage
        #THROWING STUFF
        if self.sword.mode == "Not Thrown":
            self.count = 0
            self.sword.rect.x = self.player.rect.x + self.player.iS/2
            self.sword.rect.y = self.player.rect.y + self.player.iS/2
        if self.sword.mode == "Thrown":
            self.count += 1
            if self.sword.direction == "Right":
                self.sword.speedX = 30
            elif self.sword.direction == "Left":
                self.sword.speedX = -30
            elif self.sword.direction == "Up":
                self.sword.speedY = -30
            elif self.sword.direction == "Down":
                self.sword.speedY = 30
        if self.count >= 25:
            self.sword.mode = "Not Thrown"
            self.count = 0
            self.sword.speedX = 0
            self.sword.speedY = 0
            self.sword.rect.x = self.player.rect.x + self.player.iS/2
            self.sword.rect.y = self.player.rect.y + self.player.iS/2
        #PLAYER 2
        if self.player2.mode == "Cant Copy":
            self.cloneTimer += 1
            if self.cloneTimer >= 20:
                self.cloneTimer = 0
                self.player2.mode = "Can Copy"


        self.sword.throw()
        self.player.update()
        self.player2.update()

    def redrawAll(self, screen):
        if self.mode == "Play":
            time = pygame.font.SysFont("monospace", self.maze.iS).render("Timer: " + str(self.time), 1, (0, 0, 0))
            screen.blit(time, (330 - self.maze.iS, self.height - self.maze.iS))
            for powerUps in self.powerUps:
               pygame.draw.circle(screen, (0,0,0), (powerUps[0], powerUps[1]), self.maze.iS//4)
            if self.time == 0:
                self.winner = "Player 2 "
                self.mode = "Win"
            if self.player.health > 0:
                self.player.draw()
            if self.player2.health > 0:
                self.player2.draw()
            else:
                self.winner = "Player 1 "
                self.mode = "Win"
            self.maze.draw()
        if self.sword.mode == "Thrown":
                self.sword.draw()
        elif self.mode == "Adjust":
            begin = pygame.font.SysFont("monospace", 50).render("Press Space to Start", 1, (0, 0, 0))
            screen.blit(begin, (self.width/3.5, self.height/8))
            maze_Size = pygame.font.SysFont("monospace", 50).render("Input Maze Size: " + str(self.player.mS), 1, (0, 0, 0))
            screen.blit(maze_Size, (self.width/3.5, self.height/2))
        elif self.mode == "Start":
            initial = pygame.font.SysFont("monospace", 35).render("Press Space to Start on Easy or A to adjust", 1, (0, 0, 0))
            screen.blit(initial, (self.width / 5.5, self.height / 2.5))
        elif self.mode == "Win":
            win = pygame.font.SysFont("monospace", 55).render(self.winner + "Wins", 1,
                                                                  (0, 0, 0))
            screen.blit(win, (self.width / 3, self.height / 2.5))



    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=700, height=700, fps=60, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()

        playing = True

        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False

            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()