from ast import If
from turtle import update
import pygame
from network import Network
from helper import getActionsCounter, read_pos, make_pos

width = 500
height = 500

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

centerX = width / 2 - PLAYER_WIDTH / 2
centerY = height / 2 - PLAYER_HEIGHT / 2

RED = (255,0,0)
GREEN = (0, 255,0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        # pygame.draw.circle(win, self.color, (self.x,self.y), self.width/2)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.velocity

        if keys[pygame.K_DOWN]:
            self.y += self.velocity

        if keys[pygame.K_LEFT]:
            self.x -= self.velocity

        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        

def redrawWindow(win, player, player2):
    win.fill(WHITE)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 50, 50, GREEN)
    p2 = Player(0, 0, 50, 50, RED)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if run:
            p.move()
            redrawWindow(win, p, p2)


# p2 = Player(420, 20, 50, 50, (0, 255, 0))
# p3 = Player(20, 420, 50, 50, (0, 0, 255))
# p4 = Player(220, 220, 80, 80, (155, 155, 0))

# Players = (p1,p2,p3,p4)

main()
