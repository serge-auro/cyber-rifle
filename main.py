import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Cyber Rifle')
icon = pygame.image.load('image/icon_0.jpg')
pygame.display.set_icon(icon)


running = True
while running:
    pass


pygame.quite()