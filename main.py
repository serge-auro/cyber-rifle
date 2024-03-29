import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Cyber Rifle')
icon = pygame.image.load('image/icon_01.png')
pygame.display.set_icon(icon)


target_image = pygame.image.load('image/target_0.png')
target_width = 50
target_height = 50

target_x = random.randrange(0, SCREEN_WIDTH - target_width)
target_y = random.randrange(0, SCREEN_HEIGHT - target_height)

bg_image = pygame.image.load('image/bg_0.jpg')


pygame.display.set_icon(target_image)



running = True
while running:
    pass


pygame.quite()