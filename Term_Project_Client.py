#############################
# Sockets Client Demo
# by Rohan Varma
# adapted by Kyle Chin
#############################
import pygame
import socket
import threading
from queue import Queue
from Classes import *
import random

HOST = "128.237.207.144"  # put your IP address here if playing on multiple computers
PORT = 45455

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((HOST,PORT))
print("connected to server")

def handleServerMsg(server, serverMsg):
  server.setblocking(1)
  msg = ""
  command = ""
  while True:
    msg += server.recv(10).decode("UTF-8")
    command = msg.split("\n")
    while (len(command) > 1):
      readyMsg = command[0]
      msg = "\n".join(command[1:])
      serverMsg.put(readyMsg)
      command = msg.split("\n")

# events-example0.py from 15-112 website
# Barebones timer, mouse, and keyboard events



####################################
# customize these functions
####################################

class PygameGame(object):

    def init(self):
        self.player = Player()
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
        if keyCode == pygame.K_RIGHT:
            self.player.gottaGoFastX(5)
        elif keyCode == pygame.K_LEFT:
            self.player.gottaGoFastX(-5)
        if keyCode == pygame.K_DOWN:
            self.player.gottaGoFastY(5)
        elif keyCode == pygame.K_UP:
            self.player.gottaGoFastY(-5)
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

    def timerFired(self, dt):
        self.player.update()
        pass

    def redrawAll(self, screen):
        self.player.draw()
        self.maze.draw()


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
    def run(self, serverMsg = None, server = None):

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

serverMsg = Queue(100)
threading.Thread(target = handleServerMsg, args = (server, serverMsg)).start()

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()



