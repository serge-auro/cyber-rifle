import pygame
import random

pygame.init()

target_x = 0
target_y = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
def change_target_xy():
    target_x = random.randrange(0, SCREEN_WIDTH - target_width)
    target_y = random.randrange(0, SCREEN_HEIGHT - target_height)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Cyber Rifle')
icon = pygame.image.load('image/icon_01.png')
pygame.display.set_icon(icon)


target_image = pygame.image.load('image/target_0.png')
target_width = 51
target_height = 100

change_target_xy()

# Загрузка изображения фона
bg_image = pygame.image.load('image/bg_0.jpg')
# Установка шрифта для счетчика очков
font = pygame.font.Font(None, 36)
score = 0


running = True
while running:
    # Отображение фоновой картинки
    screen.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                pygame.mouse.set_visible(False)
                score += 100
                pygame.display.update()
                pygame.time.Clock().tick(60)
                pygame.display.set_caption(f'Score: {score} x:{target_x} y:{target_y}')
                pygame.mouse.set_visible(True)
                change_target_xy()
                screen.blit(target_image, (target_x, target_y))
            else:
                pygame.mouse.set_visible(False)
                score -= 50
                pygame.display.update()
                pygame.time.Clock().tick(60)
                pygame.display.set_caption(f'Score: {score} x:{target_x} y:{target_y}')
                pygame.mouse.set_visible(True)
                change_target_xy()
                screen.blit(target_image, (target_x, target_y))

    screen.blit(target_image, (target_x, target_y))
    # Отображение счетчика очков
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()


pygame.quite()