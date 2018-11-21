import pygame
from Classes import *
from setup import *
#Framework by Lucas Peraza


class PygameGame(object):

    def init(self):
        self.mode = "Start"
        self.image = "Ice Zombie.png"
        self.image2 = "Masked Orc.png"
        self.player = Player(self.image)
        self.player2 = Player(self.image2)
        self.maze = Maze()


    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if self.mode == "Play":
            if keyCode == pygame.K_RIGHT:
                self.player.gottaGoFastX(5)
            elif keyCode == pygame.K_LEFT:
                self.player.gottaGoFastX(-5)
            if keyCode == pygame.K_DOWN:
                self.player.gottaGoFastY(5)
            elif keyCode == pygame.K_UP:
                self.player.gottaGoFastY(-5)
            if keyCode == pygame.K_d:
                self.player2.gottaGoFastX(5)
            elif keyCode == pygame.K_a:
                self.player2.gottaGoFastX(-5)
            if keyCode == pygame.K_s:
                self.player2.gottaGoFastY(5)
            elif keyCode == pygame.K_w:
                self.player2.gottaGoFastY(-5)
        elif self.mode == "Start":
            if keyCode == pygame.K_RIGHT and 15 <= self.player.mS <= 63:

                self.player.mS += 4
                self.player.iS = round(1 / self.player.iS * 700) + 1
                self.player.rect.x = round(1 / self.player.mS * 700) + 1
                self.player.rect.y = round(1 / self.player.mS * 700) + 1
                self.player2.mS += 4
                self.player2.iS = round(1/self.player.iS*700) + 1
                self.player2.rect.x = round(1/self.player.mS * 700) + 1
                self.player2.rect.y = round(1 / self.player.mS * 700) + 1
                self.maze.mS += 4
                self.maze.iS = round(1 / self.maze.mS * 700) + 1
                self.maze.lst = maze(lstMaker(self.maze.mS-1), self.maze.mS)
                self.player.image = pygame.transform.scale(pygame.image.load(self.image),((round(1 / self.player.mS * 700) - 1, round(1 / self.player.mS * 700) - 1)))
                self.player2.image = pygame.transform.scale(pygame.image.load(self.image2),((round(1 / self.player.mS * 700) - 1, round(1 / self.player.mS * 700) - 1)))
                self.maze.image = pygame.transform.scale(pygame.image.load("wall_mid.png"), (self.maze.iS, self.maze.iS))

            elif keyCode == pygame.K_LEFT and 17 <= self.player.mS <= 65:
                self.player.mS -= 4
                self.player.iS = round(1 / self.player.iS * 700) + 1
                self.player.rect.x = round(1 / self.player.mS * 700) + 1
                self.player.rect.y = round(1 / self.player.mS * 700) + 1
                self.player2.mS -= 4
                self.player2.iS = round(1/self.player.iS*700) + 1
                self.player2.rect.x = round(1/self.player.mS * 700) + 1
                self.player2.rect.y = round(1 / self.player.mS * 700) + 1
                self.maze.mS -= 4
                self.maze.iS = round(1 / self.maze.mS * 700) + 1
                self.maze.lst = maze(lstMaker(self.maze.mS-1), self.maze.mS)
                self.player.image = pygame.transform.scale(pygame.image.load(self.image),((round(1 / self.player.mS * 700) - 1, round(1 / self.player.mS * 700) - 1)))
                self.player2.image = pygame.transform.scale(pygame.image.load(self.image2),((round(1 / self.player.mS * 700) - 1, round(1 / self.player.mS * 700) - 1)))
                self.maze.image = pygame.transform.scale(pygame.image.load("wall_mid.png"), (self.maze.iS, self.maze.iS))
            elif keyCode == pygame.K_SPACE:
                self.mode = "Play"
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
        for locations in self.maze.locations:
            if locations[0] - self.maze.iS/2 <= self.player.rect.x <= locations[0] + self.maze.iS/2 and locations[1] - self.maze.iS/2 <= self.player.rect.y <= locations[1] + self.maze.iS/2:
                self.player.rect.x = self.player.oldX
                self.player.rect.y = self.player.oldY
            if locations[0] - self.maze.iS/2 <= self.player2.rect.x <= locations[0] + self.maze.iS/2 and locations[1] - self.maze.iS/2 <= self.player2.rect.y <= locations[1] + self.maze.iS/2:
                self.player2.rect.x = self.player2.oldX
                self.player2.rect.y = self.player2.oldY
        self.player.update()
        self.player2.update()

    def redrawAll(self, screen):
        if self.mode == "Play":
            self.player.draw()
            self.player2.draw()
            self.maze.draw()
        elif self.mode == "Start":
            begin = pygame.font.SysFont("monospace", 50).render("Press Space to Start", 1, (0, 0, 0))
            screen.blit(begin, (self.width/3.5, self.height/8))
            maze_Size = pygame.font.SysFont("monospace", 50).render("Input Maze Size: " + str(self.player.mS), 1, (0, 0, 0))
            screen.blit(maze_Size, (self.width/3.5, self.height/2))



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