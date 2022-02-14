import pygame
from network import Network
from helper import getActionsCounter
from player import Player
from server import width, height, WHITE

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, player, player2):
    win.fill(WHITE)
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if run:
            p.move()
            redrawWindow(win, p, p2)


main()
