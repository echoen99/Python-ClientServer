import pygame

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